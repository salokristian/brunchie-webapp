from django.urls import path
from collection import views

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view(),
         name="get_post_restaurants"),
    path('restaurants/<int:pk>/', views.RestaurantDetails.as_view(),
         name="get_put_delete_restaurant"),
    # path('restaurants/<int:pk_rest>/reviews/'),
    # path('restaurants/<int:pk_rest>/reviews/<int:pk_rew>/'),
    path('restaurants/<int:pk_rest>/servings/', views.ServingList.as_view()),
    path(
        'restaurants/<int:pk_rest>/servings/<int:pk_serv>/',
        views.ServingDetails.as_view()
    ),
]
