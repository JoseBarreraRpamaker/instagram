from django.db import models

# Create your models here.
from django.contrib.auth.models import User, update_last_login
from django.db.models.fields import NullBooleanField



class Users(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)   # blank puede estar vacio el campo.

    birthdat = models.DateField(blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)





class Profile(models.Model):


    user = models.OneToOneField(User , on_delete=models.CASCADE)
    website = models.URLField(max_length=200,blank=True) 
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15,blank=True)


    pcture = models.ImageField(upload_to='users/pictures',blank=True,null=True)

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)



def __str__(self):
    return self.user.username


 

