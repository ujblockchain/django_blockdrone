from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("browse-pilots", views.browse_pilots, name="browse-pilots"),
    path("job-review", views.job_review, name="job-review"),
    path("job-request", views.job_request, name="job-request"),
    path("accounts/login", views.login, name="login"),
    path("accounts/logout", views.logout, name="logout"),
    path("accounts/signup", views.sign_up, name="sign-up"),
]
