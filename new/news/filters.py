from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms
# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    date = DateFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Date',
        widget=forms.DateInput(attrs={'type':'date'})
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'title': ['icontains'],  # Поиск по заголовку (icontains - содержит)
            'author': ['exact'],  # Точное совпадение автора
            #'time_in': ['gte', 'lte'],
            # Фильтрация по дате публикации (gte - больше или равно, lte - меньше или равно)
        }
