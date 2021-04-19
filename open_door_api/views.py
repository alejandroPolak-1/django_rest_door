# from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import UserProfile, Door
from .serializers import UserProfileSerializers, DoorSerializers

@api_view(['GET', 'POST'])
def users_api_view(request):
        
    # List
    if request.method == 'GET':
        # queryset
        # users            = UserProfile.objects.all().values('name', 'email', 'dni')
        users            = UserProfile.objects.all()
        users_serializer = UserProfileSerializers(users, many= True)
                  
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
        doors_serializer = DoorSerializers(doors, many= True)
                
        return Response(doors_serializer.data, status = status.HTTP_200_OK)


    # Create
    elif request.method == 'POST':
        door_serializer = DoorSerializers(data = request.data)
        # validación
        if door_serializer.is_valid():
            door_serializer.save()
            return Response(door_serializer.data, status = status.HTTP_201_CREATED)
        return Response(door_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def door_detail_view(request, pk=None):
    # queryset (consulta)
    door = Door.objects.filter(id = pk).first()

    # validación
    if door: 
        # one user, de
        if request.method == 'GET':
            door_serializer = DoorSerializers(door)
            return Response(door_serializer.data, status = status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            door_serializer = DoorSerializers(door, request.data)
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