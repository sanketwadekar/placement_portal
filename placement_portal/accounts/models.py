from django.db import models

# Create your models here.
#student model

class studentModel(models.Model):

  registrationId = models.CharField(max_length = 100, blank = False, primary_key = True, unique = True)
  firstName = models.CharField(max_length = 100 , blank = False)
  lastName = models.CharField(max_length = 100 , blank = False)
  emailId = models.EmailField(max_length = 100 , blank = False, unique = True) 
  placementSeason = models.CharField(max_length = 100 , blank = False)
  jobPlaced = models.CharField(max_length = 100 , blank = True)
  password = models.CharField(max_length = 100 , blank = False)
  #resume = models.FileField(blank = True)

  def __str__(self):
    return self.registrationId
#company model

class companyModel(models.Model):

  #cId = models.IntegerField(primary_key = True,auto_created = True)
  name = models.CharField(max_length = 100, blank = False, unique = True)
  address = models.CharField(max_length = 100, blank = False)
  contact = models.IntegerField(max_length = 12,blank = False, unique = True)
  about = models.CharField(max_length = 50, blank = True)

  def __str__(self):
	  return self.name
# #job model
def path_to_upload_jd(instance,filename):
  return 'JD/jd_{0}'.format(instance.cName)
class jobModel(models.Model):

  #jobId = models.IntegerField(primary_key = True,unique = True,auto_created = True)
  cName = models.ForeignKey(companyModel.name,on_delete= models.SET_NULL)
  salary = models.FloatField(blank = True)
  dateOfArrival = models.DateField()
  lastDateToApply = models.DateField()
  jdFile = models.FileField(upload_to = path_to_upload_jd)

#jdTemplate model

class applicantModel(models.Model):
  jdLink = models