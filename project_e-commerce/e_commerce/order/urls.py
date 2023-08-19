from django.urls import path,include
from .views import *


urlpatterns = [
    path('orders/',OrdersList.as_view()),
    path('orders/create/',OrderCreate.as_view()),
    path('ordersDetail/update/<int:pk>/',OrdersDetail.as_view(),),

    
]