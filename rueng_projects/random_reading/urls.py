from django.urls import path
from random_reading import views as random_reading_views

urlpatterns = [
    path('', random_reading_views.article_detail, name='random_reading'),
]