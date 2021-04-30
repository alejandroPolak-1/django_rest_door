from rest_framework import serializers
from .models import Personal, Door, PersonalByDoors

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'


class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'
        
   

class PersonalByDoorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalByDoors
        fields = '__all__'
