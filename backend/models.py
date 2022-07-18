from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField



# Create your models here.

class Contact(models.Model):
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.email

class JobAdvert(models.Model):
    user = models.ForeignKey(User, related_name='useraccount', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    category = models.CharField( max_length = 50, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    proglanguage =  models.CharField(max_length=200, null=True, blank=True)
    published = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('advert_info', args=(str(self.id)))
    
class Freelancer(models.Model):
    user = models.ForeignKey(User, related_name='userfreelanceraccount', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField( max_length = 50, null=True, blank=True)
    pricemin = models.IntegerField(null=True, blank=True)
    pricemid = models.IntegerField(null=True, blank=True)
    pricemax = models.IntegerField(null=True, blank=True)
    priceextra = models.IntegerField(null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    proglanguage =  models.CharField(max_length=200, null=True, blank=True)
    deliveryDaysForPricemin = models.IntegerField(null=True, blank=True)
    deliveryDaysForPricemid = models.IntegerField(null=True, blank=True)
    deliveryDaysForPricemax = models.IntegerField(null=True, blank=True)
    deliveryDaysForPriceextra = models.IntegerField(null=True, blank=True)
    published = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('freelancer_info', args=(str(self.id)))
    
class Comment(models.Model):
    freelancer = models.ForeignKey(Freelancer, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.freelancer.title, self.name)
    