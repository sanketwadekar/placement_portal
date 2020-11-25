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
# def path_to_upload_jd(instance,filename):
#   return 'JD/jd_{0}'.format(instance.cName)
#job model

class jobModel(models.Model):

  #jobId = models.IntegerField(primary_key = True,unique = True,auto_created = True)
  name = models.CharField(max_length = 30,unique = True,blank = False,null = True)
  cName = models.ForeignKey(companyModel,on_delete= models.CASCADE, null = True)
  salary = models.CharField(max_length = 20,blank = True)
  dateOfArrival = models.DateField()
  lastDateToApply = models.DateField()
  jdFile = models.FileField(upload_to = 'FILES/JD/')
  
  def __str__(self):
	  return self.name

#applicant model
class applicantModel(models.Model):

  statusChoices = (
    ('Hired','Hired'),
    ('Rejected','Rejected'),
    ('In Process','In Process')
  )

  user = models.ForeignKey(User, on_delete = models.CASCADE)
  jobId = models.ForeignKey(jobModel, on_delete = models.CASCADE)
  status = models.CharField(max_length = 10,choices = statusChoices)


#notice/updates model

class noticeModel(models.Model):

  name = models.CharField(max_length = 20,blank = False,null = False,default = 'Default')
  noticeFile = models.FileField(upload_to = 'FILES/NOTICE/')
  subject = models.CharField(max_length = 100,blank = False)
  date = models.DateField(default = '2020-11-12')

  def __str__(self):
    return self.name