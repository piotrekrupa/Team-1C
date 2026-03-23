from .models import Profile
from .models import Company, Vacancy, Review
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "WAD2/homepage.html")

def user_login(request):
   return render(request, "WAD2/login.html")

def user_register(request):
    return render(request, "WAD2/register.html")

# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect(reverse("forum:home"))

# @login_required
# def account(request):
#     return render(request, "account.html")

def profile_me(request):
    if not request.user.is_authenticated:
        return redirect('forum:home')
    profile = Profile.objects.get(user=request.user)
    
    return render(request, "WAD2/profile_me.html", {"profile": profile})

def profile_user(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)
    
    return render(request, "WAD2/profile_user.html", {"profile": profile})




def internship_list(request):
    vacancies = Vacancy.objects.filter(job_type='Internship')
    return render(request, 'WAD2/internships.html', {'vacancies': vacancies})

def job_list(request):
    vacancies = Vacancy.objects.filter(job_type='Job')
    return render(request, "WAD2/jobs.html", {'vacancies': vacancies})

def internship(request, internship_name_slug):
    vacancy = get_object_or_404(Vacancy, slug=internship_name_slug)
    return render(request, 'WAD2/internship.html', {'vacancy': vacancy})

def job(request, job_name_slug):
    vacancy = get_object_or_404(Vacancy, slug=job_name_slug)
    return render(request, "WAD2/job.html", {'vacancy': vacancy})

def show_company(request, company_name_slug):
    context_dict = {}
    try:
        company = Company.objects.get(slug=company_name_slug)
        context_dict['company'] = company
        context_dict['vacancies'] = Vacancy.objects.filter(company=company)
    except Company.DoesNotExist:
        context_dict['company'] = None
    return render(request, 'WAD2/company.html', context=context_dict)

def show_vacancy(request, vacancy_name_slug):
    context_dict = {}
    try:
        vacancy = Vacancy.objects.get(slug=vacancy_name_slug)
        context_dict['vacancy'] = vacancy
    except Vacancy.DoesNotExist:
        context_dict['vacancy'] = None
    if vacancy and vacancy.job_type == 'Internship':
        return render(request, 'WAD2/internship.html', context_dict)
    return render(request, 'WAD2/job.html', context_dict)