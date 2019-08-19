from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name must be 2 characters or more"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "First Name must be 2 characters or more"
        if len(postData['email']) < 0:
            errors['email'] = "Must enter an email address"
        if len(postData['email']) > 0:
            match = re.match('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email'])
            if match == None:
                errors['email'] = "Enter an valid email address"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be more than 8 characters"
        if postData['password'] != postData['confirmpassword']:
            errors['passwordcheck'] = "Please make sure your comfirmed password is correct"
        return errors
    
    def validator_for_login(self):
        loginerrors = {}
        loginerrors['invalidinfor'] = "Please make sure your email and password are correct!"
        return loginerrors

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

