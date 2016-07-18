from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SignUp(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
   
    def __str__(self):
    	return self.username


class Login(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	def __str__(self):
		return self.username





class FileType(models.Model):
	fileupload = models.FileField('')
	user = models.ForeignKey(User)

	#name = models.CharField(max_length=200)

	
		