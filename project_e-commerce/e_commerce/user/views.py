from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser,DjangoModelPermissions
from rest_framework.authentication import get_authorization_header

from .otp_utils import *
from .models import * 
from .serializers import (
    UserProfileSerializer, 
    UserAddressSerializer,
    UserSerializer,UserLoginSerializer
    
    )

from .authentication import *
from .permissions import *


class RegisterAPI(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class=UserSerializer

    def post(self,request):
        
            data=request.data
            serializer=UserSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                 serializer.save()

                 user=CustomUser.objects.get(email=request.data['email'])
                 user.set_password(request.data['password'])
                 
                 user.save()
                      
                 return Response(
                         serializer.data,status=status.HTTP_201_CREATED
                        )
            return Response(serializer.errors)
            
        
           




class UserLoginAPIView(GenericAPIView):
    

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.get(email=request.data['email'])
        serializer = UserSerializer(user)
        access_token=create_access_token(user.id)
        refresh_token=create_refresh_token(user.id)

        response=Response()

        response.set_cookie(key='refreshToken',value=refresh_token,httponly=True)
        response.data={
          'token':access_token


        }
        

        return response

class UserLogoutAPIView(GenericAPIView):
   
    permission_classes=()
    

    def post(self, request, *args, **kwargs):
         response=Response()
         response.delete_cookie('jwt')
         response.data={
             'message':'success'
         }
         return response
    
class UserViewList(viewsets.GenericViewSet):
    authentication_classes=[]
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()   
    
    def get_queryset(self):
        header=get_authorization_header(self.request)
        return 
    
class UserListView(APIView):
    permission_classes=[]
    
    def get(self, request):
        
        
        auth=get_authorization_header(request).split()
        if auth and len(auth)== 2:
            token=auth[1].decode('utf-8')
            decode_access_token(token) 
            if CustomUser.is_superuser:

             qs=CustomUser.objects.all()
             serializer=UserSerializer(qs,many=True)

             return Response(serializer.data)
                   
        
        raise AuthenticationFailed('unauthenticated')

class UserApiView(APIView):
    def get(self, request):
        auth=get_authorization_header(request).split()
        if auth and len(auth)== 2:
            token=auth[1].decode('utf-8')
            id=decode_access_token(token)

            user=CustomUser.objects.filter(pk=id).last()

            return Response(UserSerializer(user).data)
        raise AuthenticationFailed('unauthenticated')

        

    


class UserProfileViewSet(viewsets.ModelViewSet):
    

    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class UserAddressViewSet(viewsets.ModelViewSet):
    queryset=Useraddress.objects.all()
    serializer_class=UserAddressSerializer

   

# print()

@api_view(['POST'])
def verify_otp_api(request):
    email = request.data.get('email')
    otp = request.data.get('otp')

    try:
        user = CustomUser.objects.get(email=email)
        is_valid_otp = verify_otp(user, otp)

        if is_valid_otp:
            return Response({'message': 'OTP is valid'})
        else:
            return Response({'message': 'Invalid OTP'}, status=400)

    except CustomUser.DoesNotExist:
        return Response({'message': 'User not found'}, status=400)
    