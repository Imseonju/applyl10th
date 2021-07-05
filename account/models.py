from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    realname = models.CharField(max_length=10)
    s_num = models.CharField(max_length=10)
    s_dept = models.CharField(max_length=20)

    