from django.db import models
from .shopping_cart import Shopping_Cart
from .product import Products

class Shoping_Cart_Item(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1)
    shopping_cart_id = models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE,default=1)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE,default=1)

    def save_data(self):
        self.save() 
    
    @staticmethod
    def get_shoping_cart_item_by_customer(customer_id):
        return Shoping_Cart_Item.objects.filter(customer_id=customer_id)
