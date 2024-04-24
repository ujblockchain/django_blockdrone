from django.contrib import admin

from .models import Profile, Country, City, JobRequestModel, JobType, JobReviewModel

# Register your models here.
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(JobType)
admin.site.register(JobRequestModel)
admin.site.register(JobReviewModel)
