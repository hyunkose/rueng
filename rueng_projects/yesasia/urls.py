from django.urls import path
from yesasia import views as yesasia_views

urlpatterns = [
    path('yesasia_article_list/<str:view_option>/', yesasia_views.article_list, name="yesasia_article_list"),
    path('yesasia_article_list/<str:view_option>/<int:article_id>/', yesasia_views.article_detail, name='yesasia_article_detail'),
    path('yesasia_article_previous/<str:view_option>/<int:article_id>', yesasia_views.show_previous_article, name='yesasia_article_previous'),
    path('yesasia_article_next/<str:view_option>/<int:article_id>', yesasia_views.show_next_article, name='yesasia_article_next'),
]