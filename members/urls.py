
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('add_company/', views.add_company, name = 'add_company'),
    path('', views.home, name='home'),
    path('members/<slug:username>/', views.user_profile, name = 'user_profile'),
    path('members/', views.users, name = 'users'),
    path('company/<slug:slug>/', views.co_profile, name = 'co_profile'),
    path('companies/', views.co_list, name = 'companies'),
]
