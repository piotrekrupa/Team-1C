from django.urls import path
from forum import views

app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path("upload/", views.upload, name="upload"),
    path("register/", views.user_register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("internships/", views.internship_list, name="internships"),
    path("jobs/", views.job_list, name="jobs"),
    path("internships/<slug:internship_name>/", views.internship, name="internship"),
    path("jobs/<slug:job_name>/", views.job, name="job"),
    path('profile/me/', views.profile_me, name='profile_me'),
    path('profile/<str:username>/', views.profile_user, name='profile_user'),


    path('company/<slug:company_name_slug>/', views.show_company, name='show_company'),
    path('vacancy/<slug:vacancy_name_slug>/', views.show_vacancy, name='show_vacancy'),
]