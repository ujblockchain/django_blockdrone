from django.contrib import admin

from .models import Profile, Country, City, JobRequestModel, JobType, JobReviewModel


# Register your models here.


class JobRequestModelAdmin(admin.ModelAdmin):
    list_display = (
        "request_id",
        "request_name",
        "request_create_date",
        "request_update_date",
    )


class JobReviewModelAdmin(admin.ModelAdmin):
    list_display = ("review_id", "review_job", "review_pilot", "review_create_date")


class CountryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "country"]


admin.site.register(Profile)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(JobType)
admin.site.register(JobRequestModel, JobRequestModelAdmin)
admin.site.register(JobReviewModel, JobReviewModelAdmin)
