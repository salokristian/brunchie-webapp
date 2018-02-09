from django.urls import path
from collection import views

urlpatterns = [
    path('restaurants/', views.restaurant_list),
    path('restaurants/<int:pk>/', views.restaurant_details)
]