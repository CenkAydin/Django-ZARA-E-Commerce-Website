from django.db import models
from .category import Category
import datetime

class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    discount_rate = models.IntegerField(default=0)
    start_date = models.DateField(default=datetime.datetime.today)
    end_date = models.DateField(default=datetime.datetime.today)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)

    def save_data(self):
        self.save() 
    
    @staticmethod
    def get_promotion_by_category(category_id):
        return Promotion.objects.filter(category_id=category_id)
