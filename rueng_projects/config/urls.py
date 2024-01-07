from django.contrib import admin
from django.urls import path, include
from yesasia import views as yesasia_views
from yandex_news import views as yandex_news
from random_reading import views as random_reading_views
from mywordbook import views as mywordbook_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', yesasia_views.index,name='rueng_home'),
    path('yesasia/', include('yesasia.urls')),
    path('yandex/', include('yandex_news.urls')),
    path('random_reading/', include('random_reading.urls')),
    path('mywordbook/', include('mywordbook.urls')),
]
