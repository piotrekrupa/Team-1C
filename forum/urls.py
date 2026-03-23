from django.urls import path
from forum import views

app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
<<<<<<< HEAD
    # path("upload/", views.upload, name="upload"),
=======
    path("upload/", views.upload, name="upload"),
>>>>>>> 700f71adcc1facdb893457923dfb692d25a6e3fe
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    # path("logout/", views.user_logout, name="logout"),
    # path("myaccount/", views.user, name="user"),
<<<<<<< HEAD
    path("internships/", views.internship_list, name="internships"), #Next 4 lines can be replaced with 2 using listing/Listings instead.
    path("jobs/", views.job_list, name="jobs"),
    path("internships/<slug:internship_name_slug>/", views.internship, name="internship"),
    path("jobs/<slug:job_name_slug>/", views.job, name="job"),
=======
    path("internships/", views.internships, name="internships"), #Next 4 lines can be replaced with 2 using listing/Listings instead.
    path("jobs/", views.jobs, name="jobs"),
    # path("internships/<str:internship_name>/", views.internship, name="internship"),
    # path("jobs/<str:job_name>/", views.job, name="job"),
>>>>>>> 700f71adcc1facdb893457923dfb692d25a6e3fe
    path('profile/me/', views.profile_me, name='profile_me'),
    path('profile/<str:username>/', views.profile_user, name='profile_user'),


    path('company/<slug:company_name_slug>/', views.show_company, name='show_company'),
    path('vacancy/<slug:vacancy_name_slug>/', views.show_vacancy, name='show_vacancy'),
]