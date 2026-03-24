from .models import Profile, ProfileComment
from .models import Company, Vacancy, Comment , Rating
from .forms import VacancyForm, SignUpForm
from django.contrib.auth.models import User
from .forms import CommentForm, RatingForm
from django.db.models import Avg

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
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum:home')
    else:
        form = VacancyForm()
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
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            return redirect('forum:profile_me')
        
        if 'cv' in request.FILES:
            uploaded_cv = request.FILES['cv']
            if uploaded_cv.name.endswith('.pdf'):
                profile.cv = uploaded_cv
                profile.save()
            return redirect('forum:profile_me')
        
        content = request.POST.get("content")
        if content:
            ProfileComment.objects.create(author=request.user, profile=profile, content=content)
            return redirect('forum:profile_me')
    
    comments = profile.comments_received.all()

    return render(request, "WAD2/profile_me.html", {"profile": profile, "comments": comments})

def profile_user(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)
    
    if request.method == "POST":
        if request.user.is_authenticated:
            content = request.POST.get("content")
            if content:
                ProfileComment.objects.create(author=request.user, profile=profile, content=content)
                return redirect('forum:profile_user', username=username)
    
    comments = profile.comments_received.all()

    return render(request, "WAD2/profile_user.html", {"profile": profile, "comments": comments})
    




def internship_list(request):
    vacancies = Vacancy.objects.filter(job_type='internship')
    return render(request, 'WAD2/internships.html', {'vacancies': vacancies})

def job_list(request):
    vacancies = Vacancy.objects.filter(job_type='entry_level')
    return render(request, "WAD2/jobs.html", {'vacancies': vacancies})

"""
def internship(request, internship_name_slug):
    vacancy = get_object_or_404(Vacancy, slug=internship_name_slug)
    return render(request, 'WAD2/internship.html', {'vacancy': vacancy})

def job(request, job_name_slug):
    vacancy = get_object_or_404(Vacancy, slug=job_name_slug)
    return render(request, "WAD2/job.html", {'vacancy': vacancy})
"""
# replaced with one function
def vacancy_detail(request, slug):
    vacancy = get_object_or_404(Vacancy, slug=slug)
    comments = vacancy.comments.order_by('-created_at')
    comment_form = CommentForm()
    rating_form = RatingForm()

    user_rating = None
    average_rating = vacancy.ratings.aggregate(avg=Avg('value'))['avg']

    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(vacancy=vacancy, user=request.user).first()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('forum:login')

        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.vacancy = vacancy
                comment.user = request.user
                comment.save()
                return redirect('forum:vacancy', slug=vacancy.slug)

        elif 'rating_submit' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                value = rating_form.cleaned_data['value']
                Rating.objects.update_or_create(
                    vacancy=vacancy,
                    user=request.user,
                    defaults={'value': value}
                )
                return redirect('forum:vacancy', slug=vacancy.slug)

    return render(request, 'WAD2/vacancy.html', {
        'vacancy': vacancy,
        'comments': comments,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'user_rating': user_rating,
        'average_rating': average_rating,
    })

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
