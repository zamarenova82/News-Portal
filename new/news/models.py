from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    post_rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = sum(post.rating * 3 for post in self.post)
        author_comment_rating = sum(comment.rating for comment in self.comment)
        post_comment_rating = sum(comment.rating for post in self.post for comment in post.comment)
        self.rating = post_rating + author_comment_rating + post_comment_rating


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    def __str__(self):
        return self.name.title()


news = "NE"
article = "AR"

TYPE = [
    (news, "Новость"),
    (article, "Статья")
]


class Post(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=2, choices=TYPE, default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", through="PostCategory")
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title.title()}: {self.content[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.content) <= 124:
            return self.content
        else:
            return self.content[:124] + "..."



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
