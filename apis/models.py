from django.db import models



class User(models.Model):
	phone = models.CharField(max_length = 15,unique=True)
	first_name = models.CharField(max_length=30, blank=True, null=True)
	last_name = models.CharField(max_length=30, blank=True, null=True)
	email = models.CharField(max_length=30, blank=True, null=True)
	password = models.CharField(max_length=30, blank=False, null=False)

	def __str__(self):
		return self.phone
	
	# @property
	# def numbers(self):
	# 	return self.phoneBook_set.all()

class PhoneBook(models.Model):
	user = models.ForeignKey(User,default=None,on_delete=models.SET_DEFAULT)
	name = models.CharField(max_length=30,blank=False,null=False)
	number = models.CharField(max_length=10,blank=False,null=False)