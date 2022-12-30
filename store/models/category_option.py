from django.db import models
from .category_type import Category_Type

class Category_Option(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=50)
    category_type_id = models.ForeignKey(Category_Type, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.value

    @staticmethod
    def get_all_category_options():
        return Category_Option.objects.all()