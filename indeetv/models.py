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





def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class FileType(models.Model):
	fileupload = models.FileField(upload_to=user_directory_path)
	user = models.ForeignKey(User)
	newfilename = models.CharField(max_length=100)


	
		