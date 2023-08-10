from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import (
    UserProfileViewSet,
    UserAddressViewSet,
    verify_otp_api,
    RegisterAPI,
    # UserViewList,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserApiView,
    UserListView,
    
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .otp_utils import *


router=DefaultRouter()
router.register('user',UserProfileViewSet)
router.register('user-address',UserAddressViewSet)
# router.register('user-list',UserViewList)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
   
    path('register/',RegisterAPI.as_view()),  
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout-user"),
    path('authed-user/',UserApiView.as_view()),
    path('user-list/',UserListView.as_view()),

   
    path('',include(router.urls)),
    path('api/verify-otp/', verify_otp_api, name='verify_otp'),
    
]
