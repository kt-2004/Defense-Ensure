from django.db import models

class Services(models.Model):
    iconImage=models.ImageField(upload_to="adv/static/images")
    sTitle=models.CharField(max_length=255)
    sDesc=models.TextField()

class Guards(models.Model):
    gPhoto=models.ImageField(upload_to="adv/static/images")
    gName=models.CharField(max_length=255)
    gPos=models.TextField()

class Contact(models.Model):
    cName=models.CharField(max_length=255)
    cEmail=models.EmailField()
    cPhone = models.PositiveBigIntegerField()
    cMsg=models.TextField()
    
#This model is made for registeration as well as for login.
class Users(models.Model):
    uName=models.CharField(max_length=255)
    uEmail=models.EmailField()
    uPass = models.CharField(max_length=255)

class Employee(models.Model):
    eId=models.CharField(max_length=255)
    eName=models.CharField(max_length=255)
    eEmail=models.EmailField()
    eContact = models.CharField(max_length=255)
    