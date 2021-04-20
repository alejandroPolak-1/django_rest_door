# from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.hashers import make_password, check_password

from .models import UserProfile, Door
from .serializers import UserProfileSerializers, ListUserSerializers, ListDoorSerializers, CreateDoorSerializers

@api_view(['GET', 'POST'])
def users_api_view(request):
        
    # List
    if request.method == 'GET':
        # queryset
        # users          = UserProfile.objects.all().values('name', 'email', 'password', 'dni')
        users            = UserProfile.objects.all()
        users_serializer = ListUserSerializers(users, many= True)
                  
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        user_serializer = UserProfileSerializers(data = request.data)
        # validación
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    # queryset (consulta)
    user = UserProfile.objects.filter(id = pk).first()

    # validación
    if user: 
        # one user, de
        if request.method == 'GET':
            user_serializer = UserProfileSerializers(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            user_serializer = UserProfileSerializers(user, request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            user.delete()        
            return Response({"message": "User was successfully removed!"}, status = status.HTTP_200_OK)        
    # si no hay usuatio 
    return Response({"message": "No user was found with this data"}, status = status.HTTP_400_BAD_REQUEST)  



# ######## DOOR ######################
@api_view(['GET', 'POST'])
def doors_for_users_view(request):

    if request.method == 'GET':
        
        doors            = Door.objects.all()
        doors_serializer = ListDoorSerializers(doors, many= True)
        # para hashear
        for i in doors_serializer.data:
            i['hash'] = make_password(i['hash'])
                
        return Response(doors_serializer.data, status = status.HTTP_200_OK)


    # Create
    elif request.method == 'POST':
        door_serializer = CreateDoorSerializers(data = request.data)

        # validación
        if door_serializer.is_valid():
            door_serializer.save()
            # return Response(door_serializer.data, status = status.HTTP_201_CREATED)
            return Response({"message": "Door was successfully saved!"}, status = status.HTTP_201_CREATED)
        return Response(door_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def door_detail_view(request, pk=None):
    # queryset (consulta)
    door = Door.objects.filter(id = pk).first()
    
    # hasheo
    # door.hash= make_password(door.hash)
    # Para checkear la clave
    # check_password(clave, clavehashada) _> True
    
    # validación
    if door: 
        # one user, de
        if request.method == 'GET':
            # print( check_password('123asd', "pbkdf2_sha256$260000$7lbEzUlEqcL1MhN9tiJfWb$cvZYQbVHEUzJuDZXZlmYmsMfH9KHUy7ZSaytjcRQUdw="))
            # print( check_password(door.hash, make_password(door.hash))) para chequear
            door.hash= make_password(door.hash) # hasheo
            door_serializer = ListDoorSerializers(door)
            return Response(door_serializer.data, status = status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            door.hash= make_password(door.hash) # hasheo
            door_serializer = CreateDoorSerializers(door, request.data)
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

    