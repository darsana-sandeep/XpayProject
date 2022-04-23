from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Merchant(models.Model):
    auth_user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    business = models.CharField(max_length=30)
    phone = models.IntegerField()

    city = models.CharField(max_length=20)
    busi = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    website = models.CharField(max_length=100)
