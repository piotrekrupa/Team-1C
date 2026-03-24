from django import forms
from .models import Vacancy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ListingForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'company', 'location', 'job_type', 'deadline', 'url', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control upload-input'}),
            'company': forms.TextInput(attrs={'class': 'form-control upload-input'}),
            'location': forms.TextInput(attrs={'class': 'form-control upload-input', 'placeholder': 'e.g. London, Remote'}),
            'job_type': forms.Select(attrs={'class': 'form-select upload-input'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control upload-input', 'type': 'date'}),
            'url': forms.URLInput(attrs={'class': 'form-control upload-input', 'placeholder': 'https://...'}),
            'description': forms.Textarea(attrs={'class': 'form-control upload-input', 'rows': 3}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
