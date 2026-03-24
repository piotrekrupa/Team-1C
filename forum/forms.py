from django import forms
from .models import Listing
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'company', 'location', 'job_type', 'deadline_date', 'application_url', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control upload-input'}),
            'company': forms.TextInput(attrs={'class': 'form-control upload-input'}),
            'location': forms.TextInput(attrs={'class': 'form-control upload-input', 'placeholder': 'e.g. London, Remote'}),
            'job_type': forms.Select(attrs={'class': 'form-select upload-input'}),
            'deadline_date': forms.DateInput(attrs={'class': 'form-control upload-input', 'type': 'date'}),
            'application_url': forms.URLInput(attrs={'class': 'form-control upload-input', 'placeholder': 'https://...'}),
            'description': forms.Textarea(attrs={'class': 'form-control upload-input', 'rows': 3}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
