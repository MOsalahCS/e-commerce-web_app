from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
      
      class Meta:
            
       model=UserProfile
       fields=[
           
           'user',
           'avatar',
           'bio',
           
           ]
       

class UserAddressSerializer(serializers.ModelSerializer):
      
      class Meta:
            
       model=Useraddress
       fields='__all__'
       read_only_fields=['created_at','updated_at']      



