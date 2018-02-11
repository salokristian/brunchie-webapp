from django.urls import path
from collection import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name="get_post_restaurants"),
    path('restaurants/<int:pk>/', views.restaurant_details, name="get_put_delete_restaurant")
]