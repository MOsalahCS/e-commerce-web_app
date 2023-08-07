from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated

from .otp_utils import *
from .models import * 
from .serializers import (
    UserProfileSerializer, 
    UserAddressSerializer,
    UserSerializer,UserLoginSerializer
    
    )

from rest_framework_simplejwt.tokens import RefreshToken




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
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)



class UserLogoutAPIView(GenericAPIView):
   
    permission_classes=(IsAuthenticated,)
    

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserViewList(APIView):
    def get(self , request):
     try :
          users = CustomUser.objects.all()
          
          serializer = UserSerializer(users,many=True)
           
          return Response(serializer.data)
        
     except:
         return Response({"Error":"Not Found"},status=404)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class UserAddressViewSet(viewsets.ModelViewSet):
    queryset=Useraddress.objects.all()
    serializer_class=UserAddressSerializer

   

print()

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
    
    

    


