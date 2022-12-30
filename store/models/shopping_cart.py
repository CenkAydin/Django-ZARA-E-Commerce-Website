from django.db import models
from .customer import Customer

class Shopping_Cart(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)

    def save_data(self):
        self.save()

    @staticmethod
    def get_shopping_cart_by_customer(customer_id):
        return Shopping_Cart.objects.filter(customer_id=customer_id)