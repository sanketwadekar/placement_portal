from django.urls import path
from . import views

app_name = 'customAdmin'

urlpatterns = [
    path('jobs/',views.adminJobView,name = 'jobs'),
    path('view/applications/<str:jobId>',views.adminJobApplicationsView,name = 'applications'),
    path('download/<str:jobId>',views.adminDownloadCsvFile,name = 'download'),
    path('applications/change-status',views.adminChangeApplicationView,name = 'changeStatus')
]