from .models import *
from rest_framework import serializers



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields='__all__'



class ProductSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model=Products
        fields=[
            'id',
            'category',
            'name',
            'description',
            'price',
        ]