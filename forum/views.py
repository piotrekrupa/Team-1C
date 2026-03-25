from .models import Profile
from .models import Company, Vacancy
from .forms import ListingForm, SignUpForm
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, "WAD2/homepage.html")

def upload(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum:home')
    else:
        form = ListingForm()
    return render(request, "WAD2/upload.html", {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("forum:home")
    else:
        form = AuthenticationForm()

    return render(request, "WAD2/login.html", {"form": form})


def user_register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("forum:login")
    else:
        form = SignUpForm()

    return render(request, "WAD2/register.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("forum:home")

def profile_me(request):
    if not request.user.is_authenticated:
        return redirect('forum:home')
    profile, created =Profile.objects.get_or_create(user=request.user)
    
    return render(request, "WAD2/profile_me.html", {"profile": profile})

def profile_user(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)
    
    return render(request, "WAD2/profile_user.html", {"profile": profile})




def internship_list(request):
    vacancies = Vacancy.objects.filter(job_type='internship')
    return render(request, 'WAD2/internships.html', {'vacancies': vacancies})

def job_list(request):
    vacancies = Vacancy.objects.filter(job_type='entry_level')
    return render(request, "WAD2/jobs.html", {'vacancies': vacancies})

def internship(request, internship_name):
    vacancy = get_object_or_404(Vacancy, slug=internship_name)
    return render(request, 'WAD2/internship.html', {'vacancy': vacancy})

def job(request, job_name):
    vacancy = get_object_or_404(Vacancy, slug=job_name)
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
