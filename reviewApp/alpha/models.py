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
    category = models.CharField(max_length=100)
    date_released = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    desc = models.CharField(max_length=2000)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

    def __str__(self):
        return self.name
    


