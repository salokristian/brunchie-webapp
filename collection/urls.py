from django.urls import path
from collection import views

urlpatterns = [
    path('restaurants/', views.restaurant_list),
]