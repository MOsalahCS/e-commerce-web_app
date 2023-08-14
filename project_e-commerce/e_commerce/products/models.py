from django.db import models
from user.models import CustomUser


def category_image_path(instance, filename):
    return f'product/category/icons/{instance.name}/{filename}'

def product_image_path(instance, filename):
    return f'product/images/{instance.name}/{filename}'


class ProductCategory(models.Model):
    name=models.CharField(['Category name'],max_length=100)
    icon=models.ImageField(blank=True,upload_to=category_image_path)
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
    price = models.DecimalField(('Price'), max_digits=10 , decimal_places=2 )
    image = models.ImageField(blank=True,upload_to=product_image_path)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         ordering=['-created_at']

    def __str__(self):
        return self.name



  
    


