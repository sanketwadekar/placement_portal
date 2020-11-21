from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import studentModel
class CreateUserForm(forms.Form):
    class Meta:
        model = studentModel
        fields = ['registrationId', 'firstName','lastName','emailId', 'placementSeason', 'password']