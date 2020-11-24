from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerView, name = 'register'),
    path('login/', views.loginView, name = 'login'),
    path('', views.homeView, name = 'home'),
    path('logout/', views.logoutView, name = 'logout'),
    path('notice/', views.noticeView, name = 'notice')

    #path('application/', views.applicantView, name = 'application')


    
]
