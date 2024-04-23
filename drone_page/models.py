from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name


# create profile mode
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    profile = models.TextField(blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True
    )
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    hourly_rate = models.IntegerField(blank=True, null=True, default=0)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profile_pics")

    def get_absolute_url(self):
        return reverse("pilot-detail", args=[f"{self.user.username}"])

    def __str__(self):
        return f"{self.user.username} - {self.country} - {self.city}"


# # create pilot model
# class PilotModel(models.Model):
#     pilotId = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     pilot_name = ""
#     pilot_location = models.CharField(max_length=50)
#     pilot_jobs = models.IntegerField(default=0)
#     pilot_profile_description = models.TextField()
#     pilot_rate = models.IntegerField()


# class JobRequestModel(models.Model):
#     request_job_identifier = models.CharField(max_length=23)
#     request_name = models.CharField(max_length=150)
#     request_email = models.EmailField()
#     request_pilot = ""  # pull from model
#     request_job_type = models.CharField(max_length=150)
#     request_address = models.CharField(max_length=250)
#     request_extra_information = models.TextField()


# class JobReviewModel(models.Model):
#     review_id = models.CharField(max_length=23)
#     review_email = models.EmailField()
#     review_tel = models.CharField(max_length=23)
#     review_pilot = models.CharField(
#         max_length=120
#     )  # ?one-to-one with pilot or users model
#     review_rating = models.IntegerField()  # could be smaller only 1,2,3,4,5
#     review_comments = models.TextField(max_length=500)
