from turtle import screensize
from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publishedYear = models.IntegerField()
    price = models.FloatField(null=True, blank=True, default=None)


class Mobile(models.Model):

    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    price = models.FloatField(null=True, blank=True, default=None)

class Cloth(models.Model):

    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    typeCloth = models.CharField(max_length=50)
    price = models.FloatField(null=True, blank=True, default=None)

class Laptop(models.Model):

    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    screensize = models.FloatField(null=True, blank=True, default=None)
    price = models.FloatField(null=True, blank=True, default=None)

class Shoes(models.Model):

    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    price = models.FloatField(null=True, blank=True, default=None)

class Electronic(models.Model):

    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField(null=True, blank=True, default=None)