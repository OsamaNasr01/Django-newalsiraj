
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('', views.home, name='home'),
    path('members/<slug:username>/', views.user_profile, name = 'user_profile'),
    path('members/', views.users, name = 'users'),
]
