from django.db import models
from .customer import Customer

class Tel_Number(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(default=0)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,default=1)

    def save_number(self):
        self.save()

    @staticmethod
    def get_tel_numbers_by_customer(customer_id):
        return Tel_Number.objects.filter(customer_id=customer_id)