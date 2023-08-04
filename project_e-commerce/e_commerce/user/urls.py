from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserProfileViewSet,UserAddressViewSet,verify_otp_api
from .otp_utils import *
router=DefaultRouter()
router.register('user',UserProfileViewSet)
router.register('user-address',UserAddressViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api/verify-otp/', verify_otp_api, name='verify_otp'),
    
]
