from rest_framework import serializers
from .models import *

from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=CustomUser
        fields=['id','email','name','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
        
        
       
       


class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    toekn=serializers.CharField()

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



