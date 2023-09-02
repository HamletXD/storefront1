from django import forms

class Login(forms.Form):
   name = forms.CharField()
   surname = forms.CharField()
   password = forms.CharField()
   email = forms.EmailField()