from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserProfileViewSet

router=DefaultRouter()
router.register('user',UserProfileViewSet)

urlpatterns = [
    path('',include(router.urls))
    
]
  