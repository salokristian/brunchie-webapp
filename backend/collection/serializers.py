from rest_framework import serializers
from collection.models import Restaurant, Serving, BuffetMenu


class BuffetMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuffetMenu
        fields = ('name', 'items', 'price', 'serving')


class ServingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serving
        fields = (
            'pk', 'name', 'description', 'occurs_at', 'system', 'valid_until',
            'restaurant', 'buffet_menus', 'alacarte_dishes', 'reviews',
        )


class RestaurantSerializer(serializers.ModelSerializer):
    servings = ServingSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = (
            'pk', 'name', 'street_name',
            'property_number', 'city', 'servings'
        )
