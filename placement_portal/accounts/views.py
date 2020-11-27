from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import noticeModel, jobModel
from .models import applicantModel
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date
from .mailEngine import sendRegistrationMail,sendApplyMail
from .forms import CreateUserForm
from django.contrib.auth.models import User

#from .models import *
# Create your views here.

def aboutView(request):
    return render(request, 'accounts/about.html', {})
    
def registerView(request):
    if request.user.is_authenticated and request.user.is_superuser:
        redirect('customadmin:jobs')
    elif request.user.is_authenticated and not (request.user.is_superuser):
        return redirect('accounts:home')
    else:
        registerForm = CreateUserForm()
        if request.method == 'POST':
            registerForm = CreateUserForm(request.POST)
            if registerForm.is_valid():
                registerForm.save()
                user1 = registerForm.cleaned_data.get('username')
                mail = registerForm.cleaned_data.get('email')
                first_name = registerForm.cleaned_data.get('first_name')
                last_name = registerForm.cleaned_data.get('last_name')
                messages.success(
                    request, 'Account was successfully created for ' + user1)
                subject, htmplTemplateName, to = 'welcome', 'registerMailTemplate.html', mail
                sendRegistrationMail(request,subject,htmplTemplateName,to,first_name,last_name)
                return redirect('login')
    context = {'registerForm': registerForm}
    return render(request, 'accounts/register.html', context)


def loginView(request):
    if request.user.is_authenticated and request.user.is_superuser:
        redirect('customadmin:customAdminJob')
    elif request.user.is_authenticated and not (request.user.is_superuser):
        return redirect('accounts:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('customadmin:jobs')
                else:
                    return redirect('accounts:home')
            else:
                messages.info(request, 'Inavlid Credentials..')
        context = {}
        return render(request, 'accounts/login.html', context)


@login_required(login_url='accounts:login')
def homeView(request):
    if request.user.is_superuser:
        return redirect('customadmin:jobs')
    jobs = jobModel.objects.filter().order_by('-lastDateToApply')
    jobPaginator = Paginator(jobs, 6)
    page_number = request.GET.get('page')
    page_obj = jobPaginator.get_page(page_number)
    context = {'jobs': jobs, 'page_obj': page_obj}
    return render(request, 'accounts/dashboard.html', context)


def logoutView(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def noticeView(request):
    notices = noticeModel.objects.filter().order_by('-date')
    noticePaginator = Paginator(notices, 6)
    page_number = request.GET.get('page')
    page_obj = noticePaginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'accounts/notices.html', context)


@login_required(login_url='accounts:login')
def applicantView(request):
    applications = applicantModel.objects.filter(user=request.user)
    appsPaginator = Paginator(applications, 6)
    page_number = request.GET.get('page')
    page_obj = appsPaginator.get_page(page_number)
    context = {'page_obj': page_obj, 'noapplications': False}
    if not applications:
        context['noapplications'] = True
    return render(request, 'accounts/applications.html', context)


@login_required(login_url='accounts:login')
def applyToJobView(request, jobId):
    condition1 = Q(user=request.user)
    condition2 = Q(jobId=jobId)
    checkIfDatePassed = jobModel.objects.get(id = jobId)
    userObj = User.objects.get(username = request.user)
    checkIfApplied = applicantModel.objects.filter(condition1 & condition2)
    if len(checkIfApplied):
        messages.info(request, 'Already applied...')
    elif date.today()>checkIfDatePassed.lastDateToApply:
        messages.success(request, 'Cannot apply date passed..')
    else:
        applicant = applicantModel(
            user=request.user, jobId=jobModel(id=jobId), status='In Process')
        applicant.save()
        sendApplyMail(request,"Job Application","applyMailTemplate.html",[userObj.email],checkIfDatePassed.name,checkIfDatePassed.cName)
        messages.success(request, 'Applied successfully...')

    return redirect('accounts:home')
