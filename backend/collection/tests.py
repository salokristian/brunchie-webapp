from django.test import TestCase, Client
from django.core import serializers
from django.urls import reverse
from collection.models import Restaurant
from collection.serializers import RestaurantSerializer
from rest_framework import status
import json

# Create your tests here.
class GetRestaurantsTestCase(TestCase):
    def setUp(self):
        self.kiila = Restaurant.objects.create(name="Kiila", review="It was ok.", score=4)
        self.testrest = Restaurant.objects.create(name="TestRest", review="Amazing!!", score=1)
        self.sunn = Restaurant.objects.create(name="Ravintola Sunn", review="Cool place.", score=5)
        self.client = Client()

    def test_get_restaurants(self):
        response = self.client.get(reverse('get_post_restaurants'))
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_valid_restaurant(self):
        response = self.client.get(reverse('get_put_delete_restaurant', kwargs={"pk": self.sunn.pk}))
        restaurant = Restaurant.objects.get(pk=self.sunn.pk)
        serializer = RestaurantSerializer(restaurant)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_invalid_restaurant(self):
        response = self.client.get(reverse('get_put_delete_restaurant', kwargs={"pk": 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PostRestaurantTestCase(TestCase):
    def setUp(self):
        self.valid_restaurant = {
            'name': 'Malmin Lentokentta',
            'review': 'Too much airplanes',
            'score': 2,
        }
        self.invalid_restaurant = {
            'name': 'Treffipubi',
        }


    def test_post_valid_restaurant(self):
        response = self.client.post(reverse('get_post_restaurants'), data=json.dumps(self.valid_restaurant), content_type='application/json')
        restaurant = Restaurant.objects.get(name=self.valid_restaurant['name'])
        serializer = RestaurantSerializer(restaurant)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

 
    def test_post_duplicate_restaurant(self):
        Restaurant.objects.create(**self.valid_restaurant)
        response = self.client.post(reverse('get_post_restaurants'), data=json.dumps(self.valid_restaurant), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_post_invalid_restaurant(self):
        response = self.client.post(reverse('get_post_restaurants'), data=json.dumps(self.invalid_restaurant), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Restaurant.objects.filter(name=self.invalid_restaurant['name']).exists())
        