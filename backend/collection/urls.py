from django.urls import path
from collection import views

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view(),
         name="get_post_restaurants"),
    path('restaurants/<int:pk>/', views.RestaurantDetails.as_view(),
         name="get_put_delete_restaurant")
]
