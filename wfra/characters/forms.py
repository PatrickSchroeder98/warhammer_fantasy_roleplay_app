from django import forms
from .models import Characters


class CharactersForm(forms.ModelForm):
    class Meta:
        model = Characters
        fields = ('name', 'species')  # Fields to include in the form

        # Optionally customize widgets or labels
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Character Name'}),
            'species': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Character Species'}),
        }
        labels = {
            'name': 'Character Name',
            'species': 'Species',
        }