from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserProfileViewSet,UserAddressViewSet

router=DefaultRouter()
router.register('user',UserProfileViewSet)
router.register('user-address',UserAddressViewSet)
urlpatterns = [
    path('',include(router.urls))
    
]
  