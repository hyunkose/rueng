from django.urls import path
from account import views as account_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('login/', account_view.login_view ,name='login'),
    path('logout/', account_view.logout_view, name='logout'),
    path('signup/', account_view.signup ,name='signup'),
]

