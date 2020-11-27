from django.contrib import admin
from  .models import *
# Register your models here.

class applicantAdmin(admin.ModelAdmin):
    list_display = ('user','jobId','status')
    #list_per_page = 10
    list_filter = ('status','jobId',)

class jobAdmin(admin.ModelAdmin):
    list_display = ('name','cName', 'dateOfArrival')
    #list_per_page = 10
    list_filter = ('dateOfArrival', )

admin.site.register(companyModel)
admin.site.register(jobModel, jobAdmin)
admin.site.register(noticeModel)
admin.site.register(applicantModel,applicantAdmin)