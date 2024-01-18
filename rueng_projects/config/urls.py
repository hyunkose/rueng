from django.contrib import admin
from django.urls import path, include
from yesasia import views as yesasia_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', yesasia_views.index,name='rueng_home'),
    path('yesasia/', include('yesasia.urls')),
    path('yandex/', include('yandex_news.urls')),
    path('random_reading/', include('random_reading.urls')),
    path('mywordbook/', include('mywordbook.urls')),
    path('accounts/', include('account.urls')),
]
