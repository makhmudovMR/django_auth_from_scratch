from django.db import models

# Create your models here.

class AuthSession(models.Model):
    hash = models.CharField(max_length=500)
    myuserId = models.IntegerField()

class MyUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)