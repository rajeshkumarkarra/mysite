'''
Installation

This package is designed for Python 3 and Django 1.10+. Install via:

pip install django-phone-field

Then add 'phone_field' to your INSTALLED_APPS setting.
Usage

In your models.py:

from django.db import models
from phone_field import PhoneField


class MyModel(models.Model):
    name = models.CharField(max_length=128)
    phone = PhoneField(blank=True, help_text='Contact phone number')


from django.db import models
from phone_field import PhoneField

# Create your models here.

class Client(models.Model):
	name = models.CharField(max_length=60)
	email = models.EmailField()
	phone = PhoneField(blank=True, help_text='Contact phone number')
	message = models.TextField()
	
	def __str__(self):
		return self.email

'''

from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email