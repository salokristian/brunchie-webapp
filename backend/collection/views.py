from django.shortcuts import get_object_or_404
from rest_framework import generics
from collection.models import Restaurant, Serving
from collection.serializers import *


class RestaurantList(generics.ListCreateAPIView):
    """
    List all restaurants or create a new one.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a restaurant.
    The serving field is read-only in this endpoint,
    servings can be modified at restaurants/rest_pk/servings/serv_pk/.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ServingList(generics.ListAPIView):
    """
    List all servings of a restaurant.
    """
    serializer_class = ServingSerializer

    def get_queryset(self):
        pk_rest = self.kwargs.get('pk_rest')
        return Serving.objects.filter(restaurant=pk_rest)


class ServingDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a specific serving.
    """
    serializer_class = ServingSerializer
    queryset = Serving.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        filter['restaurant'] = self.kwargs.get('pk_rest')
        filter['pk'] = self.kwargs.get('pk_serv')
        return get_object_or_404(queryset, **filter)

