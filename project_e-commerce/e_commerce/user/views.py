from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED
from rest_framework.exceptions import AuthenticationFailed
from .otp_utils import *
from .models import * 
from .serializers import UserProfileSerializer,UserAddressSerializer,UserSerializer,UserLoginSerializer

class RegisterAPI(APIView):
    def post(self,request):
        
            data=request.data
            serializer=UserSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                 serializer.save()

                 user=CustomUser.objects.get(email=request.data['email'])
                 user.set_password(request.data['password'])
                 
                 user.save()
                      
                 return Response(
                         serializer.data,status=HTTP_201_CREATED
                        )
            return Response(serializer.errors)
            
        
           




# class LoginAPI(APIView):
#         def post(self,request):
#                 username=request.data['username']
#                 password=request.data['password']
                  
#                 user=User.objects.get(username=username,password=password)
#                 if user is None:
#                      raise AuthenticationFailed('No')
                
#                 return Response({'message':'Loged In'})







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
    
    

    


