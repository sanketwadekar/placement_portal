from django.urls import path
from . import views

urlpatterns = [
    path('jobs/',views.adminJobView,name = 'customAdminJob'),
    path('view/applications/<str:jobId>',views.adminJobApplicationsView,name = 'customAdminApplications')
]