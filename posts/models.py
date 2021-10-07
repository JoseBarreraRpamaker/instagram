from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


from users.models import Profile
# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)



