from django import forms
from .models import Listing
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'company', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]