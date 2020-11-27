from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template,render_to_string 
from django.template import Context 
from django.conf import settings
from django.shortcuts import render

def sendRegistrationMail(request,subject,htmlTemplateName,receipents,first_name,last_name):
    subject, from_email, to = subject, settings.EMAIL_HOST_USER, receipents
    htmlTemplate = get_template('accounts/registerMailTemplate.html')
    context = {'first_name':first_name,'last_name':last_name}
    #html template

    html_content = render_to_string('accounts/registerMailTemplate.html',context)

    #attach files
    #msg.attach_file(path = 'path/to/file')
    #send mail

    res = send_mail(subject, "hello",from_email,[to],html_message = html_content)
    if res!=1:
        print("email process failed...")
    else:
        print("notification fired...") 

def sendApplyMail(request,subject,htmlTemplateName,receipents,job_name,company_name):
    subject, from_email, to = subject, settings.EMAIL_HOST_USER, receipents
    htmlTemplate = get_template('accounts/registerMailTemplate.html')
    context = {'job_name':job_name,'company_name':company_name}
    #html template

    html_content = render_to_string('accounts/applyMailTemplate.html',context)

    #attach files
    #msg.attach_file(path = 'path/to/file')
    #send mail

    res = send_mail(subject, "hello",from_email,[to],html_message = html_content)
    if res!=1:
        print("email process failed...")
    else:
        print("notification fired...") 

# def sendHiredMail(request,subject,htmlTemplateName,receipents = [],job_name,company_name):
#     subject, from_email, to = subject, settings.EMAIL_HOST_USER, receipents
#     htmlTemplate = get_template('accounts/hiredMailTemplate.html')
#     context = {'job_name':job_name,'company_name':company_name}
#     #html template

#     html_content = render_to_string('accounts/hiredMailTemplate.html',context)

#     #attach files
#     #msg.attach_file(path = 'path/to/file')
#     #send mail

#     res = send_mail(subject, "hello",from_email,[to],html_message = html_content)
#     if res!=1:
#         print("email process failed...")
#     else:
#         print("notification fired...") 

# def sendHiredMail(request,subject,htmlTemplateName,receipents = [],job_name,company_name):
#     subject, from_email, to = subject, settings.EMAIL_HOST_USER, receipents
#     htmlTemplate = get_template('accounts/hiredMailTemplate.html')
#     context = {'job_name':job_name,'company_name':company_name}
#     #html template

#     html_content = render_to_string('accounts/rejectedMailTemplate.html',context)

#     #attach files
#     #msg.attach_file(path = 'path/to/file')
#     #send mail

#     res = send_mail(subject, "hello",from_email,[to],html_message = html_content)
#     if res!=1:
#         print("email process failed...")
#     else:
#         print("notification fired...") 
