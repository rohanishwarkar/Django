from django.db import models

# Create your models here.
class User(models.Model):
	phone = models.CharField(max_length = 15,unique=True)
	first_name = models.CharField(max_length=30, blank=True, null=True)
	last_name = models.CharField(max_length=30, blank=True, null=True)
	email = models.CharField(max_length=30, blank=True, null=True)
	password = models.CharField(max_length=30, blank=False, null=False)