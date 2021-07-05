from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Apply(models.Model):
    motive = models.TextField(max_length=500)
    service = models.TextField(max_length=500)
    pac = models.TextField(max_length=500)
    conflict = models.TextField(max_length=500)
    aspire = models.TextField(max_length=100)
    s_time = DateTimeField()
    image = models.ImageField(upload_to = "crud/", blank = True, null = True)
    name = models.CharField(max_length=10)
    dept = models.CharField(max_length=30)
    snum = models.CharField(max_length=10) 
