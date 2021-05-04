# from django.shortcuts import render

# # Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password

from .models import Personal, Door, PersonalByDoors
from .serializer import PersonalSerializer, DoorSerializer, PersonalByDoorsSerializer, ListDoorSerializer, ListPersonalSerializer

'''
PERSONAL
'''

@api_view(['GET', 'POST'])
def personal_api_view(request):
        
    if request.method == 'GET':
        personal            = Personal.objects.all()
        personal_serializer = ListPersonalSerializer(personal, many= True)
        return Response(personal_serializer.data, status = status.HTTP_200_OK)
    
        
    # Create
    elif request.method == 'POST':
        personal_serializer =PersonalSerializer(data = request.data)
        # validación
        if personal_serializer.is_valid():
            personal_serializer.save()
            return Response(personal_serializer.data, status = status.HTTP_201_CREATED)
        return Response(personal_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def personal_detail_api_view(request, pk=None):
    personal = Personal.objects.filter(id = pk).first()

    # validación
    if personal: 
        # one personal, de
        if request.method == 'GET':
            personal_serializer = ListPersonalSerializer(personal)
            return Response(personal_serializer.data, status = status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            personal_serializer = PersonalSerializer(personal, request.data)
            if personal_serializer.is_valid():
                personal_serializer.save()
                return Response(personal_serializer.data, status = status.HTTP_200_OK)
            return Response(personal_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            personal.delete()        
            return Response({"message": "Personal was successfully removed!"}, status = status.HTTP_200_OK)        
    # si no hay usuatio 
    return Response({"message": "No personal was found with this data"}, status = status.HTTP_400_BAD_REQUEST)  



'''
DOOR
'''
    
@api_view(['GET', 'POST'])
def door_api_view(request):
        
    if request.method == 'GET':
        door            = Door.objects.all()
        door_serializer = ListDoorSerializer(door, many= True)
        
        for i in door_serializer.data:
            i['hash'] = make_password(i['hash'])
                
        return Response(door_serializer.data, status = status.HTTP_200_OK)
        
        
      # Create
    elif request.method == 'POST':
        door_serializer = DoorSerializer(data = request.data)
        # validación
        if door_serializer.is_valid():
            door_serializer.save()
            return Response(door_serializer.data, status = status.HTTP_201_CREATED)
        return Response(door_serializer.errors)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def door_detail_api_view(request, pk=None):
    door = Door.objects.filter(id = pk).first()

    # validación
    if door: 
        # one door, de
        if request.method == 'GET':
            door_serializer = ListDoorSerializer(door)
            door.hash= make_password(door.hash) # hasheo

            return Response(door_serializer.data, status = status.HTTP_200_OK)

        # elif request.method == 'POST':
        #     door_serializer = DoorSerializer(data = request.data)
        #     print(request.data['hash'])
            
        #     print(check_password('1234asdf',request.data['hash'] ))
        #         # validación
        #     if door_serializer.is_valid():
        #         # door_serializer.save()

        #         return Response({"message": "Acceso Permitido!"}, status = status.HTTP_201_CREATED)
        #     return Response(door_serializer.errors)

        # Update
        elif request.method == 'PUT':
            door_serializer = DoorSerializer(door, request.data)
            if door_serializer.is_valid():
                door_serializer.save()
                return Response(door_serializer.data, status = status.HTTP_200_OK)
            return Response(door_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            door.delete()        
            return Response({"message": "Door was successfully removed!"}, status = status.HTTP_200_OK)        
    # si no hay usuatio 
    return Response({"message": "No door was found with this data"}, status = status.HTTP_400_BAD_REQUEST)  


  
'''
DOOR - PERSONAL . -> TABLA INTERMEDIA
'''
        
        
@api_view(['GET', 'POST'])
def door_personal_api_view(request):
        
    if request.method == 'GET':
        door_personal            = PersonalByDoors.objects.all()
        door_personal_serializer = PersonalByDoorsSerializer(door_personal, many= True)
        return Response(door_personal_serializer.data, status = status.HTTP_200_OK)


     # Create
    elif request.method == 'POST':
        door_personal_serializer = PersonalByDoorsSerializer(data = request.data)
        # validación
        if door_personal_serializer.is_valid():
            door_personal_serializer.save()
            return Response(door_personal_serializer.data, status = status.HTTP_201_CREATED)
        return Response(door_personal_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def door_personal_detail_api_view(request, pk=None):
    door_personal = PersonalByDoors.objects.filter(id = pk).first()

    # validación
    if door_personal: 
        # one door_personal, de
        if request.method == 'GET':
            door_personal_serializer = PersonalByDoorsSerializer(door_personal)
            return Response(door_personal_serializer.data, status = status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            door_personal_serializer = PersonalByDoorsSerializer(door_personal, request.data)
            if door_personal_serializer.is_valid():
                door_personal_serializer.save()
                return Response(door_personal_serializer.data, status = status.HTTP_200_OK)
            return Response(door_personal_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            door_personal.delete()        
            return Response({"message": "The personal relationship and door have been removed successfully!"}, status = status.HTTP_200_OK)        
    # si no hay usuatio 
    return Response({"message": "No personal relationship and door was found with this data"}, status = status.HTTP_400_BAD_REQUEST)