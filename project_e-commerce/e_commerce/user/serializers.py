from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator


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



class UserLoginSerializer(serializers.Serializer):
    

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def Validate(self, email, password):
        user = None

        if email and password:
            user = authenticate(username=email, password=password)
        else:
            raise serializers.ValidationError(
                ("Enter an email and password."))

        return user

class VerifyUser_EmailSerialzier(serializers.Serializer):
    """
    Serializer class to verify OTP.
    """
    email = serializers.CharField(max_length=255)
    otp = serializers.CharField(max_length=6)

    def Validate_Email(self, value):
        queryset = CustomUser.objects.filter(email=value)
        if not queryset.exists():
            return Response(status=404)
        return value
    
    def validate(self, validated_data):
        email = (validated_data.get('email'))
        otp = validated_data.get('otp')

        queryset = email.objects.get(email=email)

        queryset.check_verification(security_code=otp)

        return validated_data
