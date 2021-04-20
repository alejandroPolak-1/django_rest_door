from rest_framework import serializers
from .models import UserProfile, Door

from django.contrib.auth.hashers import make_password, check_password

# modelo para crear y actualizar
class UserProfileSerializers(serializers.ModelSerializer):
            
    class Meta:
        model = UserProfile
        # exclude= ['password']
        fields = '__all__' 
        # fields = ( 'name', 'email','dni')
        
    # PARA ENCRIPTAR PASSWORD al crear
    def create(self,validated_data):
        user = UserProfile(**validated_data)
        user.set_password(validated_data['password'])
        user.save()  ##este save es del modelo, no del serializador, porque esta llamando a la instancia
        return user
    
    # PARA ENCRIPTAR PASSWORD al actualizar
    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save() ##este save es del modelo, no del serializador
        return updated_user
    
    #para Listar porque este serializador usamos para actualizar, por lo tanto no podemos  usar fields = ( 'name', 'email','dni')
    #  funcion que llama a la autamatizacion y retorna un diccionario clave: valor
    # def to_representation(self,instance):
    #     # Puedo cambiar las claves sin cambiar el modelo en base datos
    #     return {
    #         'id': instance.id,    #instance['id'], en el caso de usar values en el view, pero trae todo el objeto
    #         'name': instance.name,
    #         'email': instance.email,
    #         'dni': instance.dni,
    #         'password': instance.password
    #     }


#  PARA LISTAR USUARIOS PERSONALIZADA
class ListUserSerializers(serializers.ModelSerializer):
            
    class Meta:
        model = UserProfile
        fields = '__all__' 
        
    def to_representation(self,instance):
        # Puedo cambiar las claves sin cambiar el modelo en base datos
        return {
            'id': instance.id,    #instance['id'], en el caso de usar values en el view, pero trae todo el objeto
            'name': instance.name,
            'email': instance.email,
            'dni': instance.dni,
            'password': instance.password
        }
        
#  PARA LISTAR USUARIOS EN CONSULTA DE DOORS
class UsersDoorSerializer(serializers.ModelSerializer):
            
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email')
        

# Serializador de las Puertas    #    
class DoorSerializers(serializers.ModelSerializer):
    # users_door = UserProfileSerializers(many = True) # Para trer lso datos del usuario, sin esto solo trae el ID
    # users_door = ListUserSerializers(many = True) # Lo trae con los datos detalladas en este modelo, mas resumido
    users_door = UsersDoorSerializer(many = True) # Lo trae con los datos detalladas en este modelo, mas resumido
    
    
    class Meta:
        model = Door
        # fields = ('id', 'name', 'hash', 'users_door')
        fields= '__all__' 
        
     
  
    


