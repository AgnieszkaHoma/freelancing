from dataclasses import field
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.views.generic import ListView
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# Create your views here.

def home(request):
    return render(request, 'backend/index.html')

class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'backend/register.html'
    success_url = reverse_lazy('loginPage')

def loginPage(request):
    
    page = 'loginPage'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password1 = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username=username, password=password1)   
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
                       
    context = {'page': page}
    return render(request, 'backend/loginPage.html', context)

def signout(request):
    logout(request)
    return redirect('home')

def all_jobsadvert(request):
    jobs = JobAdvert.objects.all()
    # p = Paginator(JobAdvert.objects.all(), 3)
    # page = request.GET.get('page')
    # jobss = p.get_page(page)
    # nums = "c" * jobss.paginator.num_pages
    return render(request, 'backend/jobs_adverts.html', {'jobs': jobs})
    # return render(request, 'backend/jobs_adverts.html', {'jobs': jobs, 'jobss': jobss, 'nums':nums})

def all_freelancers(request):
    freelancers = Freelancer.objects.all()
    p = Paginator(Freelancer.objects.all(), 5)
    page = request.GET.get('page')
    jobss = p.get_page(page)
    nums = "c" * jobss.paginator.num_pages
    return render(request, 'backend/freelancers.html', {'freelancers': freelancers, 'jobss': jobss, 'nums':nums})

def about(request):   
    return render(request, 'backend/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'backend/message_send.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'backend/contact.html', context)

def advert_info(request, job_id):
    job = JobAdvert.objects.get(pk=job_id)
    return render(request, 'backend/advert_info.html', {'job': job})

def freelancer_info(request, freelancer_id):
    freelancer = Freelancer.objects.get(pk=freelancer_id)
    return render(request, 'backend/freelancer_info.html', {'freelancer': freelancer})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        freelancers = Freelancer.objects.filter(title__contains=searched)
        return render(request, 'backend/search.html', {'searched': searched, 'freelancers': freelancers})
    else:
        return render(request, 'backend/search.html', {})
    
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'backend/profile.html', {"user" : user})

def addjob(request):
    if request.method == 'POST':
        form = NewJobForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'backend/success_add.html')
    form = NewJobForm()
    context = {'form': form}
    return render(request, 'backend/add_job.html', context)

def addfreelancer(request):
    submitted=False
    if request.method == 'POST':
        form = NewFreelancerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'backend/success_add.html')
    form = NewFreelancerForm()
    context = {'form': form}
    return render(request, 'backend/add_freelancer.html', context)

class UserEditProfileView(LoginRequiredMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'backend/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    
class AddCommentView(CreateView):
    model = Comment 
    form_class = CommentForm 
    template_name = 'backend/add_comment.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.freelancer_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('freelancers')

def contact_list(request):
    contact_list = Contact.objects.all().order_by('-date')
    return render(request, 'backend/contact_list.html', {'contact_list': contact_list})

class DeleteFreelancerView(LoginRequiredMixin, DeleteView):
    model = Freelancer
    template_name = 'backend/delete_freelancer.html'
    success_url = reverse_lazy('freelancers')
    
class DeleteJobView(LoginRequiredMixin, DeleteView):
    model = JobAdvert
    template_name = 'backend/delete_job.html'
    success_url = reverse_lazy('jobs_adverts')