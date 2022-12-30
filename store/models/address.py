from django.db import models
from .country import Country

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    unit_number = models.IntegerField(default=0)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE,default=1)

    def save_address(self):
        self.save()

    @staticmethod
    def get_all_addresses():
        return Address.objects.all()