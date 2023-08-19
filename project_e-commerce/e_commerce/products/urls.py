from django.urls import path,include
from .views import *


urlpatterns = [
    path('products/',ProductsList.as_view()),
    path('products/create/',ProductCreate.as_view()),
    path('products/update/<int:pk>/',ProductDetail.as_view(),),

    
]