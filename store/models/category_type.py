from django.db import models
from .category import Category

class Category_Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_category_types():
        return Category_Type.objects.all()

    # @staticmethod
    # def get_all_category_types():
    #     return Category_Type.objects.filter(category_id = Category_Type.category_id)
        
