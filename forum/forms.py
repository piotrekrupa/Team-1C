from django import forms
from .models import Vacancy, Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ListingForm(forms.ModelForm):
    company_name = forms.CharField(max_length=128, label="Company", 
        widget=forms.TextInput(attrs={
            'class': 'form-control upload-input', 
            'placeholder': 'Company Name'
        })
    )
    class Meta:
        model = Vacancy
        fields = ['title', 'location', 'job_type', 'deadline', 'url', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control upload-input'}),
            'location': forms.TextInput(attrs={'class': 'form-control upload-input', 'placeholder': 'e.g. London, Remote'}),
            'job_type': forms.Select(attrs={'class': 'form-select upload-input'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control upload-input', 'type': 'date'}),
            'url': forms.URLInput(attrs={'class': 'form-control upload-input', 'placeholder': 'https://...'}),
            'description': forms.Textarea(attrs={'class': 'form-control upload-input', 'rows': 3}),
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        c_name = self.cleaned_data.get('company_name')
        company_obj, _ = Company.objects.get_or_create(name=c_name)
        instance.company = company_obj
        if commit:
            instance.save()
        return instance

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
