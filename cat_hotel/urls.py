from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user', views.login_user, name='login_user'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('cat_hotels', views.cat_hotels, name='cat_hotels'),
    path('<str:number_room>', views.cat_hotel, name='cat_hotel'),
    path('completed', views.completed, name='completed'),
    path('edit_completed', views.edit_completed, name='edit_completed'),
    path('success/', views.success, name='success'),   
]