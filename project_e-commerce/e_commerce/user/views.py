from rest_framework import viewsets

from .models import * 
from .serializers import UserProfileSerializer,UserAddressSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class UserAddressViewSet(viewsets.ModelViewSet):
    queryset=Useraddress.objects.all()
    serializer_class=UserAddressSerializer
   

    
    

    

