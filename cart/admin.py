from django.contrib import admin
from .models import Category, SubCategory, Product, MyCart, Order
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(MyCart)
admin.site.register(Order)