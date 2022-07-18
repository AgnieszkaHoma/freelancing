from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm


class RegisterForm(UserCreationForm):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
class ContactForm(ModelForm):
    email = forms.EmailField(required=True)
    title = forms.CharField(max_length=500, required=True)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000, required=True)
    class Meta:
        model = Contact
        fields = '__all__'
        
class NewJobForm(forms.ModelForm):
    title = forms.CharField(required=True)
    category = forms.CharField(required=True)
    proglanguage = forms.CharField(required=True)
    price = forms.CharField(required=True)
    class Meta:
        model = JobAdvert
        fields = ['title', 'category', 'proglanguage', 'description', 'price']
        
class NewFreelancerForm(forms.ModelForm):
    title = forms.CharField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    category = forms.CharField(required=True)
    image = forms.ImageField(required=True)
    proglanguage = forms.CharField(required=True)
    pricemin = forms.CharField(required=True)
    pricemid = forms.CharField(required=True)
    pricemax = forms.CharField(required=True)
    priceextra = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    deliveryDaysForPricemin = forms.CharField(required=True)
    deliveryDaysForPricemid = forms.CharField(required=True)
    deliveryDaysForPricemax = forms.CharField(required=True)
    deliveryDaysForPriceextra = forms.CharField(required=True)
    class Meta:
        model = Freelancer
        fields = ('title','category', 'firstname', 'lastname','pricemin', 'pricemid', 'pricemax', 'priceextra', 'email', 'phone', 'deliveryDaysForPricemin','deliveryDaysForPricemid','deliveryDaysForPricemax','deliveryDaysForPriceextra','image','proglanguage', 'description')
        
class EditProfileForm(UserChangeForm):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','password')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        