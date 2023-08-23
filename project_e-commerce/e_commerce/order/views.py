from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *   
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from user.authentication import *
from .serializers import *
from django.conf import settings
import stripe 



class OrderCreate(generics.CreateAPIView):
      permission_classes = ()
 
      authentication_classes=()
      queryset=Orders.objects.all() 
      serializer_class=OrderswriteSerializer
      
      
      def get_permissions(self):
          return super().get_permissions()
      def post(self,request,*args, **kwargs):
          
          return self.create(request,*args, **kwargs)
      
      
      def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,many=False)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
      
      def perform_create(self, serializer):
          order_total = float(Orders.total_cost)
          user = self.request.user

          try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            payment_intent = stripe.PaymentIntent.create(
                amount=int(order_total * 100),  
                currency='egp'
            )

            serializer.save(user=user, total_amount=order_total)
          except stripe.error.CardError as e:
            raise serializers.ValidationError(str(e))
      

class OrdersList(generics.ListAPIView):


 
    queryset=Orders.objects.all()
    serializer_class=OrdersreadSerializer
    

     
    def list(self,request):
        
            queryset = self.filter_queryset(self.get_queryset())
        
            serializer = OrdersreadSerializer(queryset, many=True)
            return Response(serializer.data)


class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrderswriteSerializer
    lookup_field='pk'
    permission_classes=[]

    
    
     
    def put(self, request,pk, *args, **kwargs):
            auth=get_authorization_header(request).split()
            if auth and len(auth)== 2:
                token=auth[1].decode('utf-8')
                decode_access_token(token) 
                product=get_object_or_404(Orders.objects.all(),id=pk)
                data=request.data
                serializer=OrderswriteSerializer(instance=product,data=data,partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                return Response({'succsess':'updated successfully'})
            
    def destroy(self, request,pk,*args, **kwargs):
          auth=get_authorization_header(request).split()
          if auth and len(auth)== 2:
                token=auth[1].decode('utf-8')
                decode_access_token(token) 
                order=get_object_or_404(Orders.objects.all(),id=pk)
                
                order.delete()
                return Response({'detail':'product deleted successfully'})
          raise AuthenticationFailed('not authed')