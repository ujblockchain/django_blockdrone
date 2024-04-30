from django.urls import path
from . import views
from .views import JobRequest, JobReview

urlpatterns = [
    path("", views.index, name="index"),
    path("browse-pilots", views.browse_pilots, name="browse-pilots"),
    path("browse-pilots/<slug:slug>", views.pilot_detail, name="pilot-detail"),
    path("job-review", JobReview.as_view(), name="job-review"),
    path("job-request", JobRequest.as_view(), name="job-request"),
    path("accounts/login", views.user_login, name="login"),
    path("accounts/logout", views.user_logout, name="logout"),
    path("accounts/signup", views.sign_up, name="sign-up"),
    path("profile/dashboard", views.user_dashboard, name="dashboard"),
    path("profile/account-settings", views.user_settings, name="account-settings"),
    path("ajax/load_cities", views.load_cities, name="ajax_load_cities"),
    path(
        "ajax/job-request",
        views.load_job_request_cities,
        name="ajax_load_job_request_cities",
    ),
    path("profile/favourites", views.user_favourites, name="favourites"),
    path("profile/blocked", views.user_blocked, name="blocked"),
    path("profile/features", views.user_blocked, name="features"),
]
