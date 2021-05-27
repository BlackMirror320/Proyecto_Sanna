from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
from django.utils import timezone

class User(models.Model):
        id=models.AutoField(primary_key=True)
        nombre=models.CharField(max_length=20)
        rut=models.CharField(max_length=20)
        mail=models.CharField(max_length=20)
        nombre=models.CharField(max_length=20)
        fono=models.IntegerField
        passwd=models.CharField(max_length=20)




# Create your models here.
