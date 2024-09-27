
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login', login_page, name='login'),
    path('register', registration_page, name='register'),
    path('profile', profile_page, name='profile'),
    path('posts', posts_page, name='posts'),

]
