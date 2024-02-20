from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("browse-pilots", views.browse_pilots, name="browse-pilots"),
    path("job-review", views.job_review, name="job-review"),
    path("job-request", views.job_request, name="job-request"),
    path("accounts/login", views.user_login, name="login"),
    path("accounts/logout", views.user_logout, name="logout"),
    path("accounts/signup", views.sign_up, name="sign-up"),
    path("profile/dashboard", views.user_dashboard, name="dashboard"),
]
