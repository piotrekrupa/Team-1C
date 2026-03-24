from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cv = models.FileField(upload_to="cvs/", blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='company_logos', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify( self.name)
        super(Company, self).save( *args, **kwargs)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    JOB_TYPE_CHOICES = [
        ('entry_level', 'Entry-Level Job'),
        ('internship', 'Internship'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    industry = models.CharField(max_length=128, blank=True)
    job_type = models.CharField(max_length=64, choices=JOB_TYPE_CHOICES, default='Internship')
    salary = models.CharField(max_length=64, blank=True)
    deadline = models.DateField(null=True, blank=True)
    url = models.URLField(blank=True) 
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.company.name}-{self.title}")
        super(Vacancy, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title

