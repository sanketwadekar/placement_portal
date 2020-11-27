from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.models import noticeModel, jobModel
from accounts.models import applicantModel
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import csv
from django.http import FileResponse
import json
import os
# Create your views here.

@login_required(login_url = 'accounts:login')
def adminJobView(request):
    jobList = jobModel.objects.filter().order_by('-lastDateToApply')
    jobPaginator = Paginator(jobList, 6)

    page = request.GET.get('page')
    page_obj = jobPaginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'customAdmin/jobs.html', context)

@login_required(login_url = 'accounts:login')
def adminJobApplicationsView(request, jobId):
    applicationsList = applicantModel.objects.filter(jobId=jobId)
    applicationsPaginator = Paginator(applicationsList, 6)
    page = request.GET.get('page')
    page_obj = applicationsPaginator.get_page(page)
    job = jobModel.objects.filter(pk=jobId)
    context = {'page_obj': page_obj, 'job': job[0]}
    return render(request, 'customAdmin/applications.html', context)

def adminDownloadCsvFile(request,jobId):
    applicationsList = applicantModel.objects.filter(jobId = jobId)
    filename = 'applicants_list_jobId-{0}.csv'.format(jobId)
    fields = ['Registration_Id','First_Name','Last_Name','Job_Id','Job_Name','Status']
    f = 0
    with open(filename,'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        if f == 0:
            csvwriter.writerow(fields)
            f = 1
        for application in applicationsList:
            row = [application.user.username,application.user.first_name,application.user.last_name,application.jobId.id,application.jobId.name,application.status]
            csvwriter.writerow(row)
    f = open(filename, 'rb')
    response = FileResponse(f)
    return response

def adminChangeApplicationView(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    JobId = body['jobId']
    Status = body['status']
    ID = body['appId']
    applicant = applicantModel.objects.get(id = ID)
    if not applicant:
        print("No application found")
    else :
       applicant.status = Status
       applicant.save()
    response = HttpResponse("")
    response.status_code = 200
    return response