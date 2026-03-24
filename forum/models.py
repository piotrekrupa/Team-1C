from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cv = models.FileField(upload_to="cvs/", blank=True, null=True)

    def __str__(self):
        return self.user.username

class Listing(models.Model):
    JOB_TYPE_CHOICES = [
        ('entry_level', 'Entry-Level Job'),
        ('internship', 'Internship'),
    ]

    title = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    location = models.CharField(max_length=128, blank=True, null=True) 
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='internship')
    deadline_date = models.DateField(blank=True, null=True)
    application_url = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"