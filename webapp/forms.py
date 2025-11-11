from django import forms
from app.catalog.models import Film, GiftCertificate, Session

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'duration', 'rating', 'release_date', 'description', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple,
        }

class GiftCertificateForm(forms.ModelForm):
    class Meta:
        model = GiftCertificate
        fields = ['code', 'balance', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['film', 'hall', 'start_time', 'end_time', 'status']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
