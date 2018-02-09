from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collection.models import Restaurant
from collection.serializers import RestaurantSerializer

@api_view(['GET', 'POST'])
def restaurant_list(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)