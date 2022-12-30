from django.db import models
from .customer import Customer
from .address import Address

class Customer_Address(models.Model):
    id = models.AutoField(primary_key=True)
    is_default = models.BooleanField(default=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,default=1)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE,default=1)

    def save_data(self):
        self.save() 
    
    @staticmethod
    def get_addresses_by_customer(customer_id):
        return Customer_Address.objects.filter(customer_id=customer_id)
        