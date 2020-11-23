from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

#from .models import *
from .forms import CreateUserForm
# Create your views here.
def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        registerForm = CreateUserForm()
        if request.method == 'POST':
            registerForm = CreateUserForm(request.POST)
            if registerForm.is_valid():
                registerForm.save()
                user1 = registerForm.cleaned_data.get('username')
                messages.success(request,'Account was successfully created for ' + user1)
                return redirect('login')
    context = {'registerForm':registerForm}
    return render(request, 'accounts/register.html', context)

def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(request,username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Inavlid Credentials..')
        context = {}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def homeView(request):
    print(request.user)
    return render(request, 'accounts/dashboard.html', context = {})

def logoutView(request):
    logout(request)
    return redirect('login')
