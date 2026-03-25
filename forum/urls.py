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
<<<<<<< HEAD
    #path("internships/<str:internship_name>/", views.internship, name="internship"),
    #path("jobs/<str:job_name>/", views.job, name="job"),
    path('vacancy/<slug:slug>/', views.vacancy_detail, name='vacancy'),
=======
    path('internships/<str:internship_name_slug>/', views.internship, name='internship'),
    path('jobs/<str:job_name_slug>/', views.job, name='job'),
>>>>>>> a11e0c4 (Add population script and fix vacancy pages)
    path('profile/me/', views.profile_me, name='profile_me'),
    path('profile/<str:username>/', views.profile_user, name='profile_user'),

    path('search/', views.search, name='search'),

    path('company/<slug:company_name_slug>/', views.show_company, name='show_company'),
]