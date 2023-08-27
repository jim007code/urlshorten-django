from django.urls import path
from django.contrib import admin

# from urlshortapp import views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('shorten/', views.shorten_url, name='shorten'),
    path('shortened/', views.get_shortened_urls, name='shortened_urls'),
]

