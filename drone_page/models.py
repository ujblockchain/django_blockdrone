from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
import uuid

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


class JobType(models.Model):
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
        """
        This method allows for quick retrieval of each profile object's canonical url path.
        """
        return reverse("pilot-detail", args=[f"{self.user.username}"])

    def __str__(self):
        return f"{self.user.username} - {self.country} - {self.city}"


class JobRequestModel(models.Model):
    request_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_name = models.CharField(max_length=150)
    request_email = models.EmailField()
    request_tel = models.CharField(
        max_length=13, help_text="Enter your phone number", null=False
    )
    request_pilot = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True
    )  # pull from model
    request_job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    request_country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        default={None: "Select a country"},
    )
    request_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    request_extra_information = models.TextField(blank=True)
    request_create_date = models.DateTimeField(auto_now_add=True)
    request_update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"job_id:{self.request_id} -pilot:{self.request_pilot.user.username} - requester:{self.request_name}"


class JobReviewModel(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review_job = models.OneToOneField(JobRequestModel, on_delete=models.PROTECT)
    # review_email = models.EmailField()
    # review_tel = models.CharField(max_length=23)
    review_pilot = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  # could be smaller only 1,2,3,4,5
    review_comment = models.TextField(max_length=500)
    review_create_date = models.DateTimeField(auto_now_add=True)
