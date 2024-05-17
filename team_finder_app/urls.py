from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/<str:game>/', views.game_profile, name='game_profile'),
    path('news/', views.news, name='news'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('search/', views.search_teammates, name='search_teammates'),
    path('logout/', views.user_logout, name='logout'),
]

