from django.urls import path
from rental_app import views


    
urlpatterns = [
    
    path("home", views.home, name="home"),
    path("addrent/<str:pk>", views.addrent, name="addrent"),
    path("Memberprofile/<str:pk>", views.profile_page, name="memberprofile"),
    path('rent/<int:movie_id>/', views.rent_movie, name='rent_movie'),
    path('return/<int:rental_id>', views.return_movie, name='return_movie'),
    
    
]
