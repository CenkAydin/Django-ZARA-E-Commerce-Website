from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.category_type import Category_Type
from .models.category_option import Category_Option
from .models.country import Country
from .models.address import Address
from .models.customer_address import Customer_Address
from .models.customer_review import Customer_Review
from .models.tel_number import Tel_Number
from .models.shopping_cart import Shopping_Cart
from .models.shopping_cart_item import Shoping_Cart_Item
from .models.payment import Payment
from .models.promotion import Promotion

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent2']

class Category_Type_Admin(admin.ModelAdmin):
    list_display = ['name', 'category_id']

class Category_Option_Admin(admin.ModelAdmin):
    list_display = ['value', 'category_type_id']

class Customer_Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

class Order_Admin(admin.ModelAdmin):
    list_display = ['product', 'quantity','price', 'customer', 'address', 'date', 'status']

class Address_Admin(admin.ModelAdmin):
    list_display = ['city', 'street', 'unit_number', 'country_id']

class Customer_Address_Admin(admin.ModelAdmin):
    list_display = ['id', 'is_default', 'customer_id', 'address_id']

class Customer_Review_Admin(admin.ModelAdmin):
    list_display = ['id', 'rating_value', 'comment', 'order_id', 'customer_id']

class Tel_Number_Admin(admin.ModelAdmin):
    list_display = ['id', 'number', 'customer_id']

class Shopping_Cart_Admin(admin.ModelAdmin):
    list_display = ['id', 'customer_id']

class Shopping_Cart_Item_Admin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'shopping_cart_id', 'product_id']

class Payment_Admin(admin.ModelAdmin):
    list_display = ['id', 'account_number', 'expiry_date', 'is_default', 'customer_id', 'order_id']

class Promotion_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'discount_rate', 'start_date', 'end_date', 'category_id']

admin.site.register(Products,AdminProduct)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, Customer_Admin)
admin.site.register(Order, Order_Admin)
admin.site.register(Category_Type, Category_Type_Admin)
admin.site.register(Category_Option, Category_Option_Admin)
admin.site.register(Country)
admin.site.register(Address, Address_Admin)
admin.site.register(Customer_Address, Customer_Address_Admin)
admin.site.register(Customer_Review, Customer_Review_Admin)
admin.site.register(Tel_Number, Tel_Number_Admin)
admin.site.register(Shopping_Cart, Shopping_Cart_Admin)
admin.site.register(Shoping_Cart_Item, Shopping_Cart_Item_Admin)
admin.site.register(Payment, Payment_Admin)
admin.site.register(Promotion, Promotion_Admin)
