from logging import PlaceHolder
from django import forms
from user_admin.models import People


    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'PlaceHolder':"********", 'data-toggle':'password'}))

class RegisterForm(forms.ModelForm):
  class Meta:
    model = People
    widgets ={
    'password': forms.PasswordInput()
    }
    fields= [
      'username',
      'password',
      'name',
      'age',
      'email'
    ]