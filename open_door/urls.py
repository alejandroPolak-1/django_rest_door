"""
CON VIEW SETS
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from open_door_api.views import UserProfileViewSet, DoorViewSet

# from open_door_api.views import UserForDoorApiView

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'doors', DoorViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
