from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)

class SubCategory(models.Model):
    name=models.CharField(max_length=40) 
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    name=models.CharField(max_length=40)
    subcat=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='prod_img')
    price=models.IntegerField()
    desc= models.TextField()

class MyCart(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    order_main_id = models.CharField(max_length=40)
    status = models.CharField(max_length= 40)  
    address= models.TextField(default='dfwfw') 
    price= models.IntegerField()        