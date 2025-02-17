from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, BaseRegisterView, IndexView, upgrade_me
from .views import CategoryList, subscribe
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view(), name='post_list'),
   # pk — это первичный ключ поста, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name ='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name ='post_delete'),
   path('login/', LoginView.as_view(template_name = 'flatpages/login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name = 'flatpages/logout.html'), name='logout'),
   path('signup/', BaseRegisterView.as_view(template_name = 'flatpages/signup.html'), name='signup'),
   path('protect/', IndexView.as_view()),
   path('upgrade/', upgrade_me, name = 'upgrade'),
   #path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail')
   path('category/<int:pk>/', CategoryList.as_view(), name='category_list'),
   path('category/<int:pk>/subscribe', subscribe, name='subscribe')
]