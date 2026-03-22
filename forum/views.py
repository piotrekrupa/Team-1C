from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
#     return redirect(reverse("forums:home"))

# @login_required
# def account(request):
#     return render(request, "WAD2/account.html")

def internships(request):
    return render(request, "WAD2/internships.html")

def jobs(request):
    return render(request, "WAD2/jobs.html")