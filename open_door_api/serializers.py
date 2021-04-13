from rest_framework import serializers
from .models import UserProfile, Door

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # fields = '__all__' 
        #fields =  ['name', 'email']
        fields = [ 'email ', 'name', 'dni', 'password'  ]
        
           
class DoorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'
        
        
