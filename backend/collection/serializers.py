from rest_framework import serializers
from collection.models import (Restaurant, Serving, Image,
    BuffetMenu, AlaCarteDish, OccursAt, Review)


class ReviewSerializer(serializers.ModelSerializer):

    def validate_score(self, score):
        if 1 <= score <= 5:
            return score
        raise serializers.ValidationError("The score must be between 1 and 5.")

    def validate_headline(self, headline):
        min_len = 10
        if len(headline) >= min_len:
            return headline
        raise serializers.ValidationError(
            "The headline needs to be at least {} chars".format(min_len)
        )

    def validate_comment(self, comment):
        min_len = 50
        if len(comment) >= min_len:
            return comment
        raise serializers.ValidationError(
            "The comment needs to be at least {} chars long.".format(min_len)
        )

    def validate(self, data):
        """
        Check that a review has either a restaurant or a serving,
        not both or neither.
        """
        both_unset = data['restaurant'] == data['serving'] is None
        both_set = data['restaurant'] and data['serving']
        if both_unset or both_set:
            raise serializers.ValidationError(
                ("A review must have either a restaurant or a serving. "
                 "You had set {}.").format("neither" if both_unset else "both")
            )
        return data

    class Meta:
        model = Review
        fields = (
            'pk', 'score', 'headline', 'comment', 'serving', 'visit_type',
            'restaurant', 'review_datetime', 'visited_date'
        )


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


class ImageSerializer(serializers.ModelSerializer):

    # validate that either restaurant or serving is chosen

    class Meta:
        model = Image
        fields = (
            'description', 'timestamp', 'file',
            'restaurant', 'serving'
        )


class ServingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serving
        fields = (
            'pk', 'name', 'description', 'occurs_at', 'system', 'valid_until',
            'restaurant', 'buffet_menus', 'alacarte_dishes', 'reviews',
            'images',
        )


class RestaurantSerializer(serializers.ModelSerializer):
    servings = ServingSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = (
            'pk', 'name', 'street_name',
            'property_number', 'city', 'servings', 'images'
        )
