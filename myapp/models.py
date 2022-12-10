from django.db import models

# Create your models here.

class Student(models.Model):
    image = models.ImageField(upload_to= 'media/')
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
