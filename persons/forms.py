from django import forms
from persons.models import Person

class AvaliadorForm(forms.ModelForm):
    class Meta:
        model = Person

