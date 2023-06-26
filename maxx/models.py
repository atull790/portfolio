
from django.contrib.auth.models import AbstractUser

from django.db import models

class new(models.Model):
    name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)

class contactmodel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    message = models.CharField(max_length=255)

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = "username"

class upload_images(models.Model):
    id = models.AutoField(primary_key=True)
    Artist_Name=models.CharField(max_length=50)
    Art_Description=models.CharField(max_length=1200)
    Type=models.CharField(max_length=1200)
    ArtWork=models.ImageField(upload_to='images')
    Price = models.DecimalField(max_digits=10, decimal_places=2)


class CartItem(models.Model):
    product = models.ForeignKey(upload_images, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    id = models.AutoField(primary_key=True)
