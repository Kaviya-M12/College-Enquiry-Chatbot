# Create your models here.
from django.db import models
class Parent(models.Model):
    Studentname=models.CharField(max_length=30)
    Parentname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.Parentname
class Staff(models.Model):
    Name=models.CharField(max_length=30)
    Department=models.CharField(max_length=6)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.Name

class Admin(models.Model):
    Name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)


class Student(models.Model):
    Name=models.CharField(max_length=30)
    Department=models.CharField(max_length=6)
    YearofPassing=models.CharField(max_length=4)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.Name





