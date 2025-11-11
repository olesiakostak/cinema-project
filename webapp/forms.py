from django import forms
from app.catalog.models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'duration', 'rating', 'release_date', 'description', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple,
        }