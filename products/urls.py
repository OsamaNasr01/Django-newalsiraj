
from django.urls import path
from . import views

urlpatterns = [

    path('product/categories/', views.p_category_list, name='p_category_list'),
    path('product/categories/add/', views.add_p_category, name='add_p_category'),
    path('product/category/<slug:slug>/', views.p_category_profile, name='p_category_profile'),
    path('product/category/update/<slug:slug>/', views.update_p_category, name='update_p_category'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('product/update/<slug:slug>/', views.update_product, name='update_product'),

]
