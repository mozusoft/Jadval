from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    date_of_birth = models.DateField(max_length=8)
    adress = models.CharField(max_length=128)
    tel_num = models.IntegerField(max_length=13)

