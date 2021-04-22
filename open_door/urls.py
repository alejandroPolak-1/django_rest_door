
from django.contrib import admin
from django.urls import path, include
from open_door_api.viewsLoginLogout import Login,Logout



# from rest_framework.routers import DefaultRouter

# # # from open_door_api.views import UserProfileViewSet, DoorViewSet
# from open_door_api.views import users_api_view, user_detail_api_view, doors_for_users_view, door_detail_view

# from open_door_api import viewa

# router = DefaultRouter()
# # router.register(r'api/',  viewset= users_api_view, basename="users")open_door_api.urlsAPI

# # router.register(r'users', UserProfileViewSet)
# # router.register(r'doors', DoorViewSet)
# router.register(r'apis', url(r'^api/', users_api_view))

# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('open_door_api.urlsAPI')),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('',Login.as_view(), name = 'login'),
    # url(r'^api/', include('open_door_api.urlsAPI')),
]
