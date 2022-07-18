from django.contrib import admin
from .models import JobAdvert, Freelancer, Comment, Contact

# Register your models here.

admin.site.register(JobAdvert)
admin.site.register(Freelancer)
admin.site.register(Comment)
admin.site.register(Contact)
