import re
from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group 
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users,admin_only
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.views.generic import View

# Create your views here.

#AUTHENTICATION
#Login
@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Entered Could be Wrong: ' +username)
            messages.info(request, 'Password Entered Could be Wrong: ' +password)

    context = {}
    return render(request, 'accounts/Authentication/Login.html',context)

#Registration
@login_required(login_url='Login')
#@allowed_users(allowed_roles=['admin'])
@admin_only
def Registration(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='cse')
            user.groups.add(group)

            messages.success(request, 'Account Created Successfully for ' + username)
            return redirect('Login')
    context = {'form': form,}
    return render(request, 'accounts/Authentication/Registration.html',context)

#LogOut
def LogOut(request):
    logout(request)
    return redirect('Login')

#Home
@login_required(login_url='Login')
def crrshome(request):
    return render(request, 'accounts/Dashboard/crrshome.html')

#UserProfile
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
def UserProfile(request):
    context = {}
    return render(request, 'accounts/Authentication/User.html',context)

#Access
@login_required(login_url='Login')
def Access(request):
    context = {}
    return render(request, 'accounts/Authentication/Access.html',context)


