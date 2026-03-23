from .models import Profile
from .forms import ListingForm, SignUpForm
from django.contrib.auth.models import User

from django.shortcuts import render
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

# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect(reverse("forums:home"))

def internships(request):
    return render(request, "WAD2/internships.html")

def jobs(request):
    return render(request, "WAD2/jobs.html")

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


