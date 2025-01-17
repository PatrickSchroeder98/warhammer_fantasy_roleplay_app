from django import forms
from .models import Characters, Fate, Resilience


class CharactersForm(forms.ModelForm):
    class Meta:
        model = Characters
        fields = ('name', 'species', 'character_class', 'career', 'career_tier', 'career_path', 'status', 'age',
                  'height', 'hair', 'eyes')  # Fields to include in the form

        # Optionally customize widgets or labels
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Character Name'}),
            'species': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Character Species'}),
        }
        labels = {
            'name': 'Character Name',
            'species': 'Species',
        }


class FateForm(forms.ModelForm):
    class Meta:
        model = Fate
        fields = ('fate', 'fortune')


class ResilienceForm(forms.ModelForm):
    class Meta:
        model = Resilience
        fields = ('resilience', 'resolve', 'motivation')

