from django.db import models

# Create your models or Tables of the Database here.
class Employee(models.Model):
    name=models.CharField(max_length=200,unique=True)
    address=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200,blank=True)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.IntegerField(unique=True)

    def __str__(self):
        return self.name
class Company(models.Model):
    name=models.CharField(max_length=200,unique=True)
    address=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200,blank=True)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=200, unique=True)
    desc=models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name
    
class Assets(models.Model):
    aNumber=models.CharField(max_length=200,unique=True)
    employee=models.ManyToManyField(Employee)
    company=models.ManyToManyField(Company)
    category=models.ManyToManyField(Category)
    tag=models.CharField(max_length=200,blank=True)
    desc=models.CharField(max_length=300,blank=True)
    
    def __str__(self):
        return self.tag
    