from django.urls import path

from .views import news_list, news_detail, add_news, edit_news

urlpatterns = [
    path('add/', add_news, name='news_add'),
    path('edit/<int:pk>/', edit_news, name='news_edit'),
    path('<int:pk>/', news_detail, name='news_detail'),
    path('', news_list, name='news_list'),
]