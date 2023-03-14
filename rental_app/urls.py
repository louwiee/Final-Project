from django.urls import path
from rental_app import views


urlpatterns = [
    path("home", views.home, name="home"),
    path("addrent/<str:pk>", views.addrent, name="addrent")
    
]