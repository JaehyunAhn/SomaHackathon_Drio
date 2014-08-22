# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from UserProfile.models import *

# Create your views here.
@csrf_exempt
def main_page(request):
    state = ""
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "successfully logged on"
                return render_to_response('searchWindow.html')
        else:
            state = "아이디와 비밀번호를 확인해주세요"
            return render_to_response('home.html',{'state':state})
    return render_to_response('home.html', {'state':state})

@csrf_exempt
def loggedon(request, username):
    return render_to_reponse('searchWindow.html')

@csrf_exempt
def messageBox(request):
    return render_to_response('msgBox.html')

@csrf_exempt
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_user(request):
    return render_to_response('register.html')
