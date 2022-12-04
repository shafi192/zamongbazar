from django.db import models

# Create your models here.

class Front(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')

class Sub_category(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics',default=None )

    def __str__(self):
        return self.name


class Product(models.Model):
    
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics',default=None)
    desc = models.CharField(max_length=200, default=None)
    def __str__(self):
        return self.name


class Sub_product(models.Model):
    
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics',default=None)
    def __str__(self):
        return self.name


class Vendor(models.Model):
    img = models.ImageField(upload_to='pics')

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Market(models.Model):
    img = models.ImageField(upload_to='pics')        