from django.shortcuts import render, redirect               #rendering of HttpResponse
from . import forms                                         #imported form for views
from django.contrib.auth.models import User                 #django's inbuilt user function
from django.contrib.auth import login, logout, authenticate #authentication 
from django.db import IntegrityError                        #if same usernames collide
from django.contrib.auth.decorators import login_required   #decorator used for access control of login

# Create your views here.

# home page before registration and login
def home(request):
	return render(request,'simple_auth/home.html')


# sign in form controller of MVC
def signin_view(request):
	sign_in_form=forms.Signin()
	if request.method=='GET':
		return render(request, 'simple_auth/signin.html', {'form':sign_in_form})
	else:
		if request.POST['password']==request.POST['password_confirm']:
			try:
				user=User.objects.create_user(request.POST['username'] , password=request.POST['password_confirm'])
				user.save()
				login(request, user)
				return redirect('landing')
			except IntegrityError:
				return render(request, 'simple_auth/signin.html', {'form':sign_in_form, 'error' : 'username already taken'})
		else:
			return render(request, 'simple_auth/signin.html' , {'form': sign_in_form, 'error':'password did not matched'} )



# login form controller of MVC
def login_view(request):
	login_form=forms.Login()
	if request.method=='GET':
		return render(request, 'simple_auth/login.html', {'form': login_form})
	else:
		user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'simple_auth/login.html', {'form': login_form , 'error':'user not found or password not matched' })
		else:
			login(request, user)
			return redirect('landing')


# page after log in 
@login_required
def landing_page(request):
	return render (request, 'simple_auth/landing.html' )

# controller for logging out
@login_required
def logout_view(request):
	if request.method=='POST':
		logout(request)
		return redirect('home')