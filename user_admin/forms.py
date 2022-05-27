from django import forms
from user_admin.models import Register

class AdminForm(forms.ModelForm):

  class Meta:
    model = Register

    fields = [
      "name",
      "password",
      "title",
      "age",
      "email"
    ]
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)