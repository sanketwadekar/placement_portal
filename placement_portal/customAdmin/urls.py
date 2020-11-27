from django.urls import path
from . import views

app_name = 'customAdmin'

urlpatterns = [
    path('jobs/',views.adminJobView,name = 'customAdminJob'),
    path('view/applications/<str:jobId>',views.adminJobApplicationsView,name = 'customAdminApplications')
]