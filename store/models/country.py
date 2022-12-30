from django.db import models

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name

    @staticmethod
    def get_all_countries():
        return Country.objects.all()
