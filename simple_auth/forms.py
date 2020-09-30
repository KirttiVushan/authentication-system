from django import forms
from django.core import validators
from django.core.exceptions import ValidationError  #for built in validation to catch bots etc.

# codes here

# signin form

class Signin(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':''}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':''}))
	password = forms.CharField(max_length=32, widget=forms.PasswordInput )
	password_confirm=forms.CharField(widget=forms.PasswordInput )
	hidden=forms.CharField(required=False, widget=forms.HiddenInput , validators=[validators.MaxLengthValidator(0)])


	
# login form

class Login(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)





