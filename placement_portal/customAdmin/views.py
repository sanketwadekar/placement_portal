from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.models import noticeModel, jobModel
from accounts.models import applicantModel
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


def adminJobView(request):
    jobList = jobModel.objects.filter().order_by('-lastDateToApply')
    jobPaginator = Paginator(jobList, 6)

    page = request.GET.get('page')
    page_obj = jobPaginator.get_page(page)
    context = {'page_obj': page_obj}
    print(context)
    return render(request, 'customAdmin/applications.html', context)


def adminJobApplicationsView(request, jobId):
    applicationsList = applicantModel.objects.filter(jobId=jobId)
    applicationsPaginator = Paginator(applicationsList, 6)

    page = request.GET.get('page')
    page_obj = applicationsPaginator.get_page(page)
    context = {'page_obj': page_obj}

    return render(request, 'customAdmin/dashboard.html', context)
