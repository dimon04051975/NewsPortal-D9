from django.urls import path, include
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, SubscriberView, CategopyListView, subscribe

from django.contrib import admin
from django.views.decorators.cache import cache_page


urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', PostsList.as_view(), name='post_list'), #http://127.0.0.1:8000/post/
    path('<int:pk>', PostDetail.as_view(), name='post_detail'), #http://127.0.0.1:8000/1
    path('create/', PostCreate.as_view(), name='post_create'),  # http://127.0.0.1:8000/news/create/
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),  # http://127.0.0.1:8000/news/pk/update/
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),  # http://127.0.0.1:8000/news/pk/delete/
    path('post/', SubscriberView.as_view(), name='subscribe'),  # http://127.0.0.1:8000/
    path('accounts/', include('allauth.urls')),
    path('categories/<int:pk>', CategopyListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    # path('<int:pk>/', cache_page(300)(PostDetail.as_view()), name='post_detail'),
    # # # кэширование страниц с новостями 5 минут
    # path('', cache_page(60)(PostList.as_view()), name='post_list'),  # кэширование главной страницы 1 минута
]
