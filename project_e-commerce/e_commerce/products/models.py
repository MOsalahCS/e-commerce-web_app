from django.db import models
from django.contrib.auth import get_user_model

User =get_user_model()



# Create your models here.

class ProductCategory(models.Model):
    name=models.CharField(['Category name'],max_length=100)
    icon=models.ImageField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name=['Product Category']
        verbose_name_plural=['Product Categories']

    def __str__(self) :
        return self.name

def get_default_product_category():
    return ProductCategory.objects.get_or_create(name='Others')[0]

class Products(models.Model):
    # seller=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey('ProductCategory',on_delete=models.SET(get_default_product_category))
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)



  
    


