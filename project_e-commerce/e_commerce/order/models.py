from django.db import models
from user.models import CustomUser,Useraddress
from products.models import Products

class Orders(models.Model):
   
   PENDING = 'P'
   COMPLETED = 'C'
   STATUS_CHOICES = ((PENDING, ('pending')), (COMPLETED, ('completed')))

   clinet = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
   status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
   payment_status = models.BooleanField(default=False)
   shipping_address = models.ForeignKey(Useraddress, related_name='shipping_orders', on_delete=models.SET_NULL, blank=True, null=True)
   billing_address = models.ForeignKey( Useraddress, related_name='billing_orders', on_delete=models.SET_NULL, blank=True, null=True)

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
        ordering = ['created_at',]

   def __str__(self):
     return self.clinet.email

   def total_cost(self):
        return round(sum([order_item.cost for order_item in self.order_items.all()]), 2)
   
   

class OrderItem(models.Model):

    order = models.ForeignKey(Orders, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey( Products, related_name="product_orders", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ['created_at',]

    def __str__(self):   
        x=str(self.product)

        return x

    def cost(self):
        return round(self.quantity * self.product.price, 2)