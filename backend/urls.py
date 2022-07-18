from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . views import UserEditProfileView, PasswordsChangeView, AddCommentView




urlpatterns = [
    path('', views.home, name='home'), 
    path('register',views.UserRegisterView.as_view(), name="register"),
    path('loginPage',views.loginPage, name="loginPage"),
    path('signout',views.signout, name="signout"),
    path('jobs_adverts',views.all_jobsadvert, name="jobs_adverts"),
    path('freelancers',views.all_freelancers, name="freelancers"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('advert/<int:job_id>/', views.advert_info, name='advert_info'),
    path('freelancer/<int:freelancer_id>/', views.freelancer_info, name='freelancer_info'),
    path('search/', views.search, name='search'),
    path('profile/<username>/', views.profile, name='profile'),
    path('add_job', views.addjob, name='add_job'),
    path('add_freelancer/', views.addfreelancer, name='add_freelancer'),
    path('edit_profile', UserEditProfileView.as_view(), name='edit_profile'),
    path('password', PasswordsChangeView.as_view(template_name='backend/change_password.html'), name = 'change_password'),
    path('freelancer/<int:pk>/add_comment', views.AddCommentView.as_view(), name='add_comment'),
    path('contact_list', views.contact_list, name='contact_list'),
    path('freelancer/<pk>/delete_freelancer', views.DeleteFreelancerView.as_view(), name="delete_freelancer"),
    path('job_advert/<pk>/delete_job', views.DeleteJobView.as_view(), name="delete_job"),
]