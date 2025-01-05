from django.db import models

# Create your models here.

class Student(models.Model):
    studentid = models.IntegerField()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    mobile = models.IntegerField()

class Management(models.Model):
    studentid = models.IntegerField()
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    mobile = models.IntegerField()

class Employees(models.Model):
    studentid = models.IntegerField()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    mobile = models.IntegerField()

class Clients(models.Model):
    studentid = models.IntegerField()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    mobile = models.IntegerField()



