from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .otp_utils import *
from .models import * 
from .serializers import UserProfileSerializer,UserAddressSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class UserAddressViewSet(viewsets.ModelViewSet):
    queryset=Useraddress.objects.all()
    serializer_class=UserAddressSerializer
   



@api_view(['POST'])
def verify_otp_api(request):
    email = request.data.get('email')
    otp = request.data.get('otp')

    try:
        user = User.objects.get(email=email)
        is_valid_otp = verify_otp(user, otp)

        if is_valid_otp:
            return Response({'message': 'OTP is valid'})
        else:
            return Response({'message': 'Invalid OTP'}, status=400)

    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=400)
    
    

    

