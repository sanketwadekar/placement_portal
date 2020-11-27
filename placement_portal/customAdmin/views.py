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
    context = {'page_obj': page_obj, 'job': page_obj[0].jobId}
    return render(request, 'customAdmin/applications.html', context)

def adminDownloadCsvFile(request,jobId):
    applicationsList = applicantModel.objects.filter(jobId = jobId)

    if len(applicationsList):
        filename = 'shortlist_jobId-{0}.csv'.format(jobId)
        filedest = 'static/downloads/{0}'.format(filename)
        fields = ['Registration_Id','First_Name','Last_Name','Job_Id','Job_Name','Status']
        f = 0
        with open(filedest,'w') as csvfile:
            print("in")
            csvwriter = csv.writer(csvfile)
            if f == 0:
                csvwriter.writerow(fields)
                f = 1
            for application in applicationsList:
                row = [application.user.username,application.user.first_name,application.user.last_name,application.jobId.id,application.jobId.name,application.status]
                csvwriter.writerow(row)
        print("file written successfully....")
        response = FileResponse(open('static/downloads/shortlist_jobId-{0}.csv'.format(jobId), 'rb'))
    else:
        response = "No applications found..."
    return response

#@login_required(login_url = 'accounts:login')
def adminChangeApplicationView(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    JobId = body['jobId']
    Status = body['status']
    ID = body['id']
    applicant = applicantModel.objects.get(id = ID)
    if not applicant:
        print("No application found")
    else :
       applicant.status = Status
       applicant.save()