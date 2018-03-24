from rest_framework import generics
from collection.models import Restaurant
from collection.serializers import RestaurantSerializer


class restaurant_list(generics.ListCreateAPIView):
    """
    List all restaurants or create a new one.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class restaurant_details(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a restaurant.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
