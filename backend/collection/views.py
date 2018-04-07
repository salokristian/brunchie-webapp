from django.shortcuts import get_object_or_404
from rest_framework import generics
from collection.models import (Restaurant, Serving, BuffetMenu,
    AlaCarteDish, OccursAt)
from collection.serializers import (ServingSerializer, RestaurantSerializer,
    BuffetMenuSerializer, AlaCarteDishSerializer, OccursAtSerializer)


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


class ServingList(generics.ListCreateAPIView):
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


class BuffetMenuList(generics.ListCreateAPIView):
    """
    List all buffet menus or create a new one.
    """
    serializer_class = BuffetMenuSerializer
    queryset = BuffetMenu.objects.all()


class BuffetMenuDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a buffet menu.
    """
    serializer_class = BuffetMenuSerializer
    queryset = BuffetMenu.objects.all()


class ServingsBuffetMenuList(generics.ListAPIView):
    """
    List buffet menus of belonging to a serving with primary key=pk_serv.
    """
    serializer_class = BuffetMenuSerializer

    def get_queryset(self):
        filter = {}
        filter['serving'] = self.kwargs.get('pk_serv', None)
        return BuffetMenu.objects.filter(**filter)


class AlaCarteDishList(generics.ListCreateAPIView):
    """
    List all ala carte dishes or create a new one.
    """
    serializer_class = AlaCarteDishSerializer
    queryset = AlaCarteDish.objects.all()


class AlaCarteDishDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an ala carte dish.
    """
    serializer_class = AlaCarteDishSerializer
    queryset = AlaCarteDish.objects.all()


class ServingsAlaCarteDishList(generics.ListAPIView):
    """
    List all ala carte dishes belonging to a serving with primary key=pk_serv.
    """
    serializer_class = AlaCarteDishSerializer

    def get_queryset(self):
        filter = {}
        filter['serving'] = self.kwargs.get('pk_serv', None)
        return AlaCarteDish.objects.filter(**filter)


class OccursAtList(generics.ListCreateAPIView):
    """
    List the occurrings of all servings or create a new one.
    """
    serializer_class = OccursAtSerializer
    queryset = OccursAt.objects.all()


class OccursAtDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an occurring.
    """
    serializer_class = OccursAtSerializer
    queryset = OccursAt.objects.all()


class ServingsOccursAtList(generics.ListAPIView):
    """
    List all occurrings of a serving with primary key=pk_serv.
    """
    serializer_class = OccursAtSerializer

    def get_queryset(self):
        filter = {}
        filter['serving'] = self.kwargs.get('pk_serv', None)
        return OccursAt.objects.filter(**filter)
