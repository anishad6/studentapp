from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,)
    phone_number = models.CharField(max_length=20)
    branch= models.CharField(max_length=20)
    per= models.FloatField()
    address= models.CharField(max_length=200)


    