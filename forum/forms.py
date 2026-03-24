from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'company', 'location', 'job_type', 'deadline_date', 'application_url', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'company': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'location': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'e.g. London, Remote'}),
            'job_type': forms.Select(attrs={'class': 'form-select custom-input'}),
            'deadline_date': forms.DateInput(attrs={'class': 'form-control custom-input', 'type': 'date'}),
            'application_url': forms.URLInput(attrs={'class': 'form-control custom-input', 'placeholder': 'https://...'}),
            'description': forms.Textarea(attrs={'class': 'form-control custom-input', 'rows': 3}),
        }