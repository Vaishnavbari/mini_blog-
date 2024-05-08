from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(registration)
class registrationadmin(admin.ModelAdmin):
     
    list_display=["id","username","password"]

@admin.register(addblog)
class addblogadmin(admin.ModelAdmin):
     
    list_display=["id","name","title","meassage","location"]