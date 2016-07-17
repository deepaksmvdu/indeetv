#files.py

from django import forms
from models import SignUp,Login,FileType


 
class SignUpForm(forms.ModelForm):
 
    username = forms.CharField(max_length=50,label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=50,label='Password')
    
    class Meta:
        model = SignUp

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50,label='Username')
    password = forms.CharField(max_length=50,label='Password')


    class Meta:
        model = Login


class Dashboard(forms.ModelForm):
    fileupload = forms.FileField()
    #name = forms.CharField()

    class Meta:
        model = FileType