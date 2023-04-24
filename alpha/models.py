from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s"% (timeNow, old_filename)
    return os.path.join('uploads/', filename)
#Product Table...
class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    average_cost = models.CharField(max_length=100)
    product_qty = models.IntegerField(null=False, blank=False, default=1)
    category = models.CharField(max_length=100)
    date_released = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)    
    desc = models.CharField(max_length=2000)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

    def __str__(self):
        return self.name
    
# Review Table...
class Review(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    product_rating = models.IntegerField()
    review_content = models.CharField(max_length=2000)     
    created_on = models.DateTimeField(auto_now_add=True)
      
 
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)  
    product_qty = models.IntegerField(null=False, blank=False, default=1)         
    created_at = models.DateTimeField(auto_now_add=True)
      
 
def catpath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s"% (timeNow, old_filename)
    return os.path.join('images/', filename)

class Category(models.Model):
    cat = models.CharField(max_length=100)
    image = models.ImageField(upload_to=catpath, null=True, blank=True)

    def __str__(self):
        return self.cat

