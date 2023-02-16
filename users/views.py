from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.template.loader import render_to_string  
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.views.generic import ListView
from django.core.paginator import Paginator



@login_required(login_url='loginpage')
def home(request):
    
    context = {
    }
    return render(request, 'users/home.html', context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username= request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Account Does Not Exist')

    context =  {}
    return render(request, 'users/login.html', context)



def logoutpage(request):
    logout(request)
    return redirect('loginpage')



