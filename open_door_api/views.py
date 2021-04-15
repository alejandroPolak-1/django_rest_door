from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view

# from django.contrib.auth.hashers import make_password, check_password

from rest_framework import viewsets

# from rest_framework.views import APIView
# from rest_framework.response import Response

from .models import UserProfile, Door
from .serializers import UserProfileSerializers, DoorSerializers
# codeh=make_password('1234')
# print(codeh)
# print(check_password('1234', codeh))

'''CON APIview'''
# class UserForDoorApiView(APIView):
#   

'''CON viewsets'''

class UserProfileViewSet(viewsets.ModelViewSet): 
    serializer_class = UserProfileSerializers
    queryset         = UserProfile.objects.all()
    
 
 
    
class DoorViewSet(viewsets.ModelViewSet):
    serializer_class = DoorSerializers
    queryset         = Door.objects.all()

