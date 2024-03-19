from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# create pilot model
class PilotModel(models.Model):
    pilotId = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    pilot_name = ""
    pilot_location = models.CharField(max_length = 50)
    pilot_jobs = models.IntegerField(default=0)
    pilot_profile_description = models.TextField()
    pilot_rate = models.IntegerField()

class JobRequestModel(models.Model):
    request_job_identifier = models.CharField(max_length=23)
    request_name = models.CharField(max_length=150)
    request_email = models.EmailField()
    request_pilot = "" # pull from model
    request_job_type = models.CharField(max_length=150)
    request_address = models.CharField(max_length=250)
    request_extra_information = models.TextField()

class JobReviewModel(models.Model):
    review_id = models.CharField(max_length=23)
    review_email = models.EmailField()
    review_tel = models.CharField(max_length=23)
    review_pilot = models.CharField(max_length=120)#?one-to-one with pilot or users model
    review_rating = models.IntegerField()#could be smaller only 1,2,3,4,5
    review_comments = models.TextField(max_length=500)
    