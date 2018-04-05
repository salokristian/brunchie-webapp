from rest_framework import serializers
from collection.models import Restaurant, Serving


class ServingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serving
        fields = (
            'pk', 'name', 'description',
            'system', 'valid_until', 'restaurant'
        )


class RestaurantSerializer(serializers.ModelSerializer):
    servings = ServingSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = (
            'pk', 'name', 'street_name',
            'property_number', 'city', 'servings'
        )
