# Create your views here.
import os
import re
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from hub.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as django_logout
from django.template import RequestContext
from utils import *
def signup(request):
	if request.method == 'POST':
		
		email=request.POST['email']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		password=request.POST['password']
		user=User.objects.create_user(
			username=email,
			email=email,
			password=password,
			first_name=first_name,
			last_name=last_name,
			)
		Student.objects.create(
			user=user)
		return HttpResponseRedirect('/login/')
	return render( request, 'hub/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username =username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/home/')
        else:
        	return HttpResponseRedirect('/login/')
    return render(request, 'hub/login.html')

def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        current_user=Student.objects.get(user=request.user)
        ip=get_client_ip(request)
        return_city_country(ip, current_user)
    return render(request, 'hub/home.html', {'current_user':current_user})

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'hub/index.html')
    else:
        current_user=Student.objects.get(user=request.user)
        return render(request, 'hub/index.html', {'current_user':current_user})

def results(request):
    if not request.user.is_authenticated():
        return render(request, 'hub/results.html')
    else:
        current_user=Student.objects.get(user=request.user)
        return render(request, 'hub/results.html', {'current_user':current_user})

def edit_info(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
    	current_user=Student.objects.get(user=request.user)
        list_skill=Skills.objects.filter(student=current_user)
    	if request.method=='POST':
    	    
    	    request.user.first_name=request.POST.get('first_name','')
    	    request.user.last_name=request.POST.get('last_name','')
    	    request.user.username=current_user.user.email=request.POST.get('email','')
    	    current_user.bio=request.POST.get('bio','')
    	    current_user.city=request.POST.get('city','')
    	    current_user.country=request.POST.get('country','')
    	    current_user.facebook_link=request.POST.get('facebook_link','')
            skill=request.POST.get('skill','')
            level=request.POST.get('level','')
            Skills.objects.create(
                name=skill,
                level=level,
                student=current_user)
            current_user.save()
            request.user.save()
            return HttpResponseRedirect('/edit_info/')
    return render(request, 'hub/edit_info.html', {'current_user':current_user, 'list_skill' :list_skill})



def image(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/')
	else:
		current_user=Student.objects.get(user=request.user)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/login/')