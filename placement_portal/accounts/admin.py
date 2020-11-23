from django.contrib import admin
from  .models import *
# Register your models here.

class applicantAdmin(admin.ModelAdmin):
    list_display = ('user','jobId','status')
    #list_per_page = 10
    list_filter = ('status','jobId',)

admin.site.register(companyModel)
admin.site.register(jobModel)
admin.site.register(noticeModel)
admin.site.register(applicantModel,applicantAdmin)