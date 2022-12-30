from django.db import models
from .customer import Customer
from .orders import Order

class Customer_Review(models.Model):
    id = models.AutoField(primary_key=True)
    rating_value = models.IntegerField()
    comment = models.CharField(max_length=255)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE,default=1)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,default=1)

    
    def save_data(self):
        self.save() 
    
    @staticmethod
    def get_reviews_by_customer(customer_id):
        return Customer_Review.objects.filter(customer_id=customer_id)
        