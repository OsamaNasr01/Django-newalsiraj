
from django.urls import path
from . import views

urlpatterns = [
    path('members/login_user/', views.login_user, name = 'login'),
    path('members/logout_user/', views.logout_user, name = 'logout'),
    path('members/register_user/', views.register_user, name = 'register'),
    path('', views.home, name='home'),
    path('members/<slug:username>/', views.user_profile, name = 'user_profile'),
    path('members/', views.users, name = 'users'),
]
