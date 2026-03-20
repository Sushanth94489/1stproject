from django.db import models
class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=15)
    password=models.CharField(max_length=100)