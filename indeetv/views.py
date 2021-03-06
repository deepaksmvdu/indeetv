import os
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from indeetv.forms import * 
from indeetv.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.conf import settings
import re
# Create your views here.


def index(request):
	return render(request, 'indeetv/login.html')


def logout_user(request):
	logout(request)
	return render(request, 'indeetv/login.html')


def signup(request):
	if request.method=='POST':

		forms = SignUpForm(request.POST)
		if User.objects.filter(username=request.POST["username"]).exists():
			return render(request, 'indeetv/signup.html',{"status":"Username Already Exists"})
		if User.objects.filter(email=request.POST["email"]).exists():
			return render(request, 'indeetv/signup.html',{"status":"Email Already Exists"})

		if forms.is_valid():
			username = request.POST["username"]
			password = request.POST["password"]

			email=request.POST["email"]
			
			user = User.objects.create_user(username=username,password=password,
				email=email)
			user.save()
			person = authenticate(username=username,password=password)
			login(request,person)
			return HttpResponseRedirect('/dashboard')
	else:
		forms = SignUpForm()
		return render(request, 'indeetv/signup.html', {'form': forms})

def login_req(request):

	if request.method=='POST':

		username = request.POST["username"]
		password = request.POST["password"]
		 
		submit = LoginForm(request.POST)
		if submit.is_valid():
			person = authenticate(username=username,password=password)
			if person is not None:

				login(request,person)
				return HttpResponseRedirect('/dashboard')
			else:
				return render_to_response('indeetv/login.html',{"status":"Wrong Credentials"},
					 context_instance=RequestContext(request))
	else:
		return render(request, 'indeetv/login.html')


@login_required(login_url='login_req')
def dashboard(request):
	loggedin_user = request.user
	if request.method =='POST':
		forms = Dashboard(request.POST,request.FILES,User)
		if forms.is_valid():
			newfilename = request.POST.get('newfilename')
			newdoc = FileType(fileupload = request.FILES['fileupload'],user=loggedin_user)
			if newfilename and newfilename != '':
				ext = re.search(r'\.(.*)', newdoc.fileupload.name).groups()[0]
				newdoc.fileupload.name = newfilename +'.'+ext
			newdoc.user = request.user
			newdoc.save()
			 
		return HttpResponseRedirect('/dashboard')

	else:
		forms = Dashboard()
	documents = FileType.objects.filter(user=request.user)
	return render_to_response(
        'indeetv/dashboard.html',
        {'documents': documents, 'form': forms},
        context_instance=RequestContext(request)
    )


 
def mediaitems(request, user_id,filename):
	data = user_id + '/' + filename
	print (data)
	return render(request, 'indeetv/mediafiles.html',{'path': data})

		
 