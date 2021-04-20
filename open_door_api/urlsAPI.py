from django.urls import path

from rest_framework.routers import DefaultRouter

from open_door_api.views import users_api_view, user_detail_api_view, doors_for_users_view, door_detail_view

# router = DefaultRouter()
# router.register(r'users',  users_api_view, basename="users")
# # router.register(r'doors', doors_for_users_view)

# urlpatterns = router.urls


urlpatterns = [
      path('users/', users_api_view, name = 'api_users'),
      path('users/<int:pk>/', user_detail_api_view, name = 'user_detail_api_view'),
      path('doors/', doors_for_users_view, name = 'api_doora'),
      path('doors/<int:pk>/', door_detail_view, name = 'user_detail_door_api_view'),
]

     