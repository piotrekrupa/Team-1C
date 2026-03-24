from django.contrib import admin
from .models import Profile, ProfileComment
from .models import Company, Vacancy


# Register your models here.
admin.site.register(Profile)
admin.site.register(ProfileComment)


class CompanyAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class VacancyAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)