from rest_framework import serializers
from collection.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'score', 'review', 'pk')