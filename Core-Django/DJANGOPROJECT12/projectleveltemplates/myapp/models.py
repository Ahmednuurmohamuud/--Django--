from django.db import models

# Create your models here.

class Employee(models.Model):
	eno = models.IntegerField()
	ename = models.CharField(max_length=30)
	empsal = models.FloatField()
	eaddr = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=30)
    sid = models.IntegerField()
    email = models.CharField(max_length=30)
    mobile = models.IntegerField()
    addr = models.CharField(max_length=50)


class Management(models.Model):
    name = models.CharField(max_length=30)
    mngid = models.IntegerField()
    email = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.CharField(max_length=50)


class Company(models.Model):
    cname = models.CharField(max_length=20)   
    addr = models.CharField(max_length=50)

class Programmer(models.Model):
	pgno=models.IntegerField()
	pgname=models.CharField(max_length=30)
	pgsal=models.FloatField()
	pgaddr=models.CharField(max_length=30)
	
	def __str__(self):
        	return self.pgname

class  SoftwareDevelopers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.EmailField()
    company = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=100)