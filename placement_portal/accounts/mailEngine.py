from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
from django.conf import settings
from django.shortcuts import render

def sendRegistrationMail(request,subject,htmlTemplateName,receipents = []):
    subject, from_email, to = subject, settings.EMAIL_HOST_USER, receipents
    htmlTemplate = get_template('templates/accounts/registerMailTemplate.html')
    context = {}
    #html template

    html_content = htmlTemplate.render(context)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
    msg.attach_alternative(html_content, "text / html") 

    #attach files
    #msg.attach_file(path = 'path/to/file')
    #send mail

    res = msg.send()
    if res!=1:
        print("email process failed...")
    else:
        print("notification fired...") 
