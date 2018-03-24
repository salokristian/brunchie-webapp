from rest_framework import generics
from collection.models import Restaurant
from collection.serializers import RestaurantSerializer


class RestaurantList(generics.ListCreateAPIView):
    """
    List all restaurants or create a new one.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a restaurant.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
