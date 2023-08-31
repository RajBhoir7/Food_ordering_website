from django.db import models

# Create your models here.


class Rest_details(models.Model):
    Rest_name = models.CharField(max_length=50)
    Owner_name = models.CharField(max_length=50)
    Email = models.EmailField()
    Owner_contact = models.BigIntegerField()
    Rest_location = models.CharField(max_length=100)
    status = models.BooleanField(default=False,null=True)


class Login_details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)