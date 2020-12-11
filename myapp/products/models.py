from __future__ import unicode_literals
from django.db.models import CharField
from django.db import models
from django_mysql.models import ListTextField
from django.contrib import admin

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        
class ProductAdmin(admin.ModelAdmin):
    model = Categories
    list_display = ['name', ] 
    list_editable = ['name', ] 

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Categories',on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=4,max_digits=15)
    min_quantity = models.IntegerField()
    description = models.TextField()
    features = models.TextField()
    image1 = models.ImageField(upload_to='products')
    image2 = models.ImageField(upload_to='products',null=True,blank=True)
    image3 = models.ImageField(upload_to='products',null=True,blank=True)
    image4 = models.ImageField(upload_to='products',null=True,blank=True)
    image5 = models.ImageField(upload_to='products',null=True,blank=True)
    is_famous_product = models.BooleanField(default=False)

    def __str__(self):
        return self.name