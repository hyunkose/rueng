from django.urls import path
from yandex_news import views as yandex_news

urlpatterns = [
    path('yandex_article_list/<str:view_option>/', yandex_news.article_list, name="yandex_article_list"),
    path('yandex_article_list/<str:view_option>/<str:article_id>/', yandex_news.article_detail, name="yandex_article_detail"),
    path('yandex_article_previous/<str:view_option>/<str:article_id>/', yandex_news.show_previous_article, name='yandex_article_previous'),
    path('yandex_article_next/<str:view_option>/<str:article_id>/', yandex_news.show_next_article, name='yandex_article_next'),
]