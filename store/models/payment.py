from django.db import models
from .orders import Order
from .customer import Customer

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    account_number = models.CharField(max_length=50)
    expiry_date = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,default=1)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE,default=1)

    def save_data(self):
        self.save() 
    
    @staticmethod
    def get_payment_by_order_id(order_id):
        return Payment.objects.filter(order_id= order_id)