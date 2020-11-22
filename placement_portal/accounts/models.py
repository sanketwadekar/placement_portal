from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#company model

class companyModel(models.Model):

  #cId = models.IntegerField(primary_key = True,auto_created = True)
  name = models.CharField(max_length = 100, blank = False, unique = True)
  address = models.CharField(max_length = 100, blank = False)
  contact = models.CharField(max_length = 12,blank = False, unique = True)
  about = models.CharField(max_length = 50, blank = True)

  def __str__(self):
	  return self.name
# # #job model
# def path_to_upload_jd(instance,filename):
#   return 'JD/jd_{0}'.format(instance.cName)
class jobModel(models.Model):

  #jobId = models.IntegerField(primary_key = True,unique = True,auto_created = True)
  cName = models.ForeignKey(companyModel,on_delete= models.SET_NULL, null = True)
  salary = models.CharField(max_length = 20,blank = True)
  dateOfArrival = models.DateField()
  lastDateToApply = models.DateField()
  jdFile = models.FileField(upload_to = 'JD/')
  
#   def __str__(self):
# 	  return self.cName

