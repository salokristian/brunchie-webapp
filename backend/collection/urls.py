from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from collection import views

urlpatterns = [
    path(
        'restaurants/',
        views.RestaurantList.as_view(),
        name="get_post_restaurants"
    ),
    path(
        'restaurants/<int:pk>/',
        views.RestaurantDetails.as_view(),
        name="get_put_delete_restaurant"
    ),
    path(
        'servings/',
        views.ServingList.as_view(),
        name="get_post_servings"
    ),
    path(
        'servings/<int:pk>/',
        views.ServingDetails.as_view(),
        name="get_put_delete_serving"
    ),
    path(
        'images/',
        views.ImageList.as_view(),
        name="get_post_images"
    ),
    path(
        'servings/buffets/',
        views.BuffetMenuList.as_view(),
        name="get_post_buffets"
    ),
    path(
        'servings/buffets/<int:pk>/',
        views.BuffetMenuDetails.as_view(),
        name="get_put_delete_buffet"
    ),
    path(
        'servings/<int:pk_serv>/buffets/',
        views.ServingsBuffetMenuList.as_view(),
        name="get_post_buffets_of_serving"
    ),
    path(
        'servings/alacartes/',
        views.AlaCarteDishList.as_view(),
        name="get_post_alacartes"
    ),
    path(
        'servings/alacartes/<int:pk>/',
        views.AlaCarteDishDetails.as_view(),
        name="get_put_delete_alacartes"
    ),
    path(
        'servings/<int:pk_serv>/alacartes/',
        views.ServingsAlaCarteDishList.as_view(),
        name="get_post_alacartes_of_serving"
    ),
    path(
        'servings/occursats/',
        views.OccursAtList.as_view(),
        name="get_post_occursats"
    ),
    path(
        'servings/occursats/<int:pk>/',
        views.OccursAtDetails.as_view(),
        name="get_put_delete_occursats"
    ),
    path(
        'servings/<int:pk_serv>/occursats/',
        views.ServingsOccursAtList.as_view(),
        name="get_post_occursats_of_serving"
    ),
    path(
        'reviews/',
        views.ReviewList.as_view(),
        name="get_post_reviews"
    ),
    path(
        'reviews/<int:pk>/',
        views.ReviewDetails.as_view(),
        name="get_put_delete_review"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
