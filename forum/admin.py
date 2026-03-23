from django.contrib import admin
from .models import Profile
from .models import Company, Vacancy, Review


# Register your models here.
admin.site.register(Profile)


class CompanyAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class VacancyAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Review)