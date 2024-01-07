from django.urls import path
from mywordbook import views as mywordbook_views

urlpatterns = [
    path('mywordbook/', mywordbook_views.mywordbook_main, name='mywordbook_main'),
]