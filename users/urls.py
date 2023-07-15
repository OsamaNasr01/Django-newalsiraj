
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
    path('users/', views.users_list, name= 'users_list' )
]