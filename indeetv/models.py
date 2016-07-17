from django.db import models

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
	fileupload = models.FileField(upload_to='')
	#name = models.CharField(max_length=200)

	
		