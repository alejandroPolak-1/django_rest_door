from rest_framework import serializers
from .models import Personal, Door, PersonalByDoors

'''
PERSONAL
'''
# Para crear, actualizar y eliminar
class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Personal
        fields = '__all__'


#  Para Listar puerta en el detalle de cada usuario
class DoorforPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Door
        fields = ("id", "name", 'ip', 'hash')

# Para implementar el listado adecuado al realizar consulta de usuarios       
class ListPersonalSerializer(serializers.ModelSerializer):
    doors  = DoorforPersonalSerializer(many = True)
    
    class Meta:
        model  = Personal
        fields = '__all__'
        # fields = ('id', 'email', 'name', 'lastname', 'dni', 'movil_user')

        

'''
DOOR
'''


# Para crear, actualizar y eliminar
class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'


#  Para Listar personal detallado en cada puerta
class PersonalforDoorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Personal
        fields = ("id", "email", "name", "lastname", "movil_user")
        
# Para implementar el listado adecuado al realizar consulta d ela puerta        
class ListDoorSerializer(serializers.ModelSerializer):
    personals = PersonalforDoorSerializer(many = True) # Lo trae con los datos detalladas en este modelo, mas resumido
    
    class Meta:
        model = Door
        fields= '__all__' 



'''
Yabla de relación
'''
# Para crearDelete
class PersonalByDoorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalByDoors
        fields = '__all__'
        
        #  Para Listar puerta en el detalle de cada usuario
class DoorbyPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Door
        fields = ("id", "name", "ip", 'hash')

class ListPersonalByDoorsSerializer(serializers.ModelSerializer):
    door     = DoorbyPersonalSerializer()
    personal = PersonalforDoorSerializer()

    class Meta:
        model    = PersonalByDoors
        fields   = '__all__'