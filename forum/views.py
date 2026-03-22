from .models import Profile
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "homepage.html")

# def user_login(request):
#     return render(request, "login.html")

# def user_register(request):
#     return render(request, "register.html")

# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect(reverse("forum:home"))

# @login_required
# def account(request):
#     return render(request, "account.html")

# def internships(request):
#     return render(request, "internships.html")

# def jobs(request):
#     return render(request, "jobs.html")

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