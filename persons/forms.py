from django import forms
from persons.models import Person

class AvaliadorForm(forms.ModelForm):
    class Meta:
        model = Person

class LoginForm(forms.Form):
    email = forms.CharField(max_length='200', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

