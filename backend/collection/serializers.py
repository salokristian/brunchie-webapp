from rest_framework import serializers
from collection.models import (Restaurant, Serving,
    BuffetMenu, AlaCarteDish, OccursAt)


class OccursAtSerializer(serializers.ModelSerializer):

    class Meta:
        model = OccursAt
        fields = ('pk', 'starts_at', 'ends_at', 'weekday', 'serving')


class AlaCarteDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlaCarteDish
        fields = ('pk', 'name', 'description', 'price', 'serving')


class BuffetMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuffetMenu
        fields = ('pk', 'name', 'items', 'price', 'serving')


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
