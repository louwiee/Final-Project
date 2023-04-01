from django.contrib import admin
from django.urls import path, include
from .views import signup_acc, login_acc, logout_acc, home

urlpatterns = [
    
    path('login/signup/', signup_acc, name='signup'),
    path('login/', login_acc, name='login'),
    path('logout/', logout_acc, name='logout'),
    
]
