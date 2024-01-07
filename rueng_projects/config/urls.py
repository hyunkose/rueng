from django.contrib import admin
from django.urls import path
from yesasia import views as yesasia_views
from yandex_news import views as yandex_news
from random_reading import views as random_reading_views
from mywordbook import views as mywordbook_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', yesasia_views.index,name='rueng_home'),

    path('yesasia_article_list/<str:view_option>/', yesasia_views.article_list, name="yesasia_article_list"),
    path('yesasia_article_list/<str:view_option>/<int:article_id>/', yesasia_views.article_detail, name='yesasia_article_detail'),
    path('yesasia_article_previous/<str:view_option>/<int:article_id>', yesasia_views.show_previous_article, name='yesasia_article_previous'),
    path('yesasia_article_next/<str:view_option>/<int:article_id>', yesasia_views.show_next_article, name='yesasia_article_next'),

    path('yandex_article_list/<str:view_option>/', yandex_news.article_list, name="yandex_article_list"),
    path('yandex_article_list/<str:view_option>/<str:article_id>/', yandex_news.article_detail, name="yandex_article_detail"),
    path('yandex_article_previous/<str:view_option>/<str:article_id>/', yandex_news.show_previous_article, name='yandex_article_previous'),
    path('yandex_article_next/<str:view_option>/<str:article_id>/', yandex_news.show_next_article, name='yandex_article_next'),


    path('random_reading/', random_reading_views.article_detail, name='random_reading'),
    
    path('mywordbook/', mywordbook_views.mywordbook_main, name='mywordbook_main'),
]
