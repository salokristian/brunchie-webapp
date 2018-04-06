from django.shortcuts import get_object_or_404
from rest_framework import generics
from collection.models import Restaurant, Serving, BuffetMenu
from collection.serializers import (ServingSerializer,
    RestaurantSerializer, BuffetMenuSerializer)


class RestaurantList(generics.ListCreateAPIView):
    """
    List all restaurants or create a new one.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a restaurant.
    The serving (ALSO INSERT OTHERS HERE) field is read-only in this endpoint,
    servings can be modified at /servings/<serv_pk>/.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ServingList(generics.ListAPIView):
    """
    List all servings.
    """
    serializer_class = ServingSerializer
    queryset = Serving.objects.all()


class ServingDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a specific serving.
    """
    serializer_class = ServingSerializer
    queryset = Serving.objects.all()


class BuffetMenuList(generics.ListAPIView):
    """
    List all buffet menus, or the menus
    of the serving with primary key=pk_serv.
    """
    serializer_class = BuffetMenuSerializer

    def get_queryset(self):
        filter = {}
        filter['serving'] = self.kwargs.get('pk_serv', None)
        if filter['serving']:
            return BuffetMenu.objects.filter(**filter)
        return BuffetMenu.objects.all()


class BuffetMenuDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a buffet menu.
    """
    serializer_class = BuffetMenuSerializer
    queryset = BuffetMenu.objects.all()
