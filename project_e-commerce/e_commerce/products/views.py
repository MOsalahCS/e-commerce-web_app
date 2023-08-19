from django.shortcuts import get_object_or_404
from .models import *   
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from user.authentication import *
from .serializers import *

class ProductsList(generics.ListAPIView):
    permission_classes=[]
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    

     
    def list(self,request):
        
            queryset = self.filter_queryset(self.get_queryset())
        
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
           


class ProductCreate(generics.CreateAPIView):
      permission_classes=[IsAdminUser]
      queryset=Products.objects.all() 
      serializer_class=ProductSerializer
      
      
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
          return serializer.save()
      
        
        
       
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    permission_classes=[]

    
    
     
    def put(self, request,pk, *args, **kwargs):
            auth=get_authorization_header(request).split()
            if auth and len(auth)== 2:
                token=auth[1].decode('utf-8')
                decode_access_token(token) 
                product=get_object_or_404(Products.objects.all(),id=pk)
                data=request.data
                serializer=ProductSerializer(instance=product,data=data,partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                return Response({'succsess':'updated successfully'})
            
    def destroy(self, request,pk,*args, **kwargs):
          auth=get_authorization_header(request).split()
          if auth and len(auth)== 2:
                token=auth[1].decode('utf-8')
                decode_access_token(token) 
                product=get_object_or_404(Products.objects.all(),id=pk)
                
                product.delete()
                return Response({'detail':'product deleted successfully'})
          raise AuthenticationFailed('not authed')

            
        

    
    
   
            
           
        
        
