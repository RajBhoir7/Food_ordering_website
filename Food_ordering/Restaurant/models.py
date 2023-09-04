from django.db import models

# Create your models here.


class Rest_details(models.Model):
    Rest_name = models.CharField(max_length=50,primary_key=True)
    Owner_name = models.CharField(max_length=50)
    Email = models.EmailField()
    Owner_contact = models.BigIntegerField()
    Rest_location = models.CharField(max_length=100)
    status = models.BooleanField(default=False,null=True)

    def __str__(self) ->str:
        return self.Rest_name
    


class Login_details(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self) ->str:
        return self.username
    

class Menu(models.Model):
    Rest_name = models.ForeignKey(Rest_details,on_delete=models.SET_NULL,null=True)
    Menu_name = models.CharField(max_length=25)
    Menu_desc = models.CharField(max_length=50)
    Menu_Price = models.IntegerField()
    Menu_img = models.ImageField(upload_to='media/')
