from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import *

# @receiver(user_logged_in,sender=registration.username)
# def login_view(sender,request,user,**kwargs):
#     print("login view ")
#     print(registration.username)
#     ip=request.META.get('REMOTE_ADDR')
#     print('HHHHHHHHHHHHHHHHHhhhHHHHHHH')
#     print(ip)
#     request.session['ip']=ip

