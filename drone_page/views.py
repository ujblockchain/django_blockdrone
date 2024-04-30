from typing import Any
import uuid
from django.forms import BaseModelForm, ValidationError
from django.shortcuts import get_object_or_404, render
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


from .forms import (
    SignUpForm,
    LoginForm,
    UpdateUserForm,
    ProfileForm,
    JobRequestsForm,
    JobReviewForm,
)
from .models import City, Country, JobType, Profile, JobRequestModel, JobReviewModel

User = get_user_model()
# Create your views here.


def sign_up(request):

    template_page = "drone_page/accounts/signup.html"

    if request.method == "POST":
        form = SignUpForm(request.POST)
        # validate the inputs
        if form.is_valid():
            # check if passwords match
            if form.cleaned_data["password1"] == form.cleaned_data["password2"]:
                new_user = User.objects.create_user(
                    username=form.cleaned_data["username"],
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["username"],
                    email=form.cleaned_data["email"],
                    user_type=form.cleaned_data["user_type"],
                    tel_number=form.cleaned_data["tel_number"],
                    password=form.cleaned_data["password1"],
                )
                # save to the database
                new_user.save()

                # redirect to login page
                return HttpResponsePermanentRedirect(reverse("login"))
        else:
            # print("not valid?")
            # print(form.errors)
            # messages.add_message(request, messages.ERROR, form.errors)
            return HttpResponseRedirect(reverse("sign-up"))
    else:
        # create form when someone lands on the page
        form = SignUpForm()

    context = {"form": form}

    return render(request, template_page, context)


# USER Related Views
def user_login(request):
    # login page
    template_page = "drone_page/accounts/login.html"

    if request.method == "POST":
        print("test")
        # get details entered into form
        form = LoginForm(request, request.POST)
        # validate the inputs
        if form.is_valid():
            # username
            username = request.POST.get("username")
            # password
            password = request.POST.get("password")

            # authenticate the user
            user = authenticate(request, username=username, password=password)

            # if the user is authenticated
            if user is not None:
                auth.login(request, user)

                return HttpResponsePermanentRedirect(reverse("dashboard"))
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, template_page, context)


def user_logout(request):

    auth.logout(request)

    request.session.flush()
    "... request"

    return HttpResponsePermanentRedirect(reverse("index"))


@login_required(login_url="login")
def user_dashboard(request):
    template_page = "drone_page/profile/dashboard.html"

    # get the user
    user_logged_in = request.user
    # get job requests?
    job_requests = JobRequestModel.objects.filter(request_pilot_id=user_logged_in.id)

    context = {
        "user_logged_in": user_logged_in,
        "user_logged_in_job_requests": job_requests,
        "user_logged_in_no_jobs": job_requests.count(),
    }
    return render(request, template_page, context)


def user_settings(request):
    # define template page to be loaded
    template_page = "drone_page/profile/account-settings.html"
    # get the user who is logged in
    user_logged_in = User.objects.get(id=request.user.id)
    print(user_logged_in.user_type)

    # create instance of form to update user information
    user_update_form = UpdateUserForm()
    # create instance of form to update user profile information
    user_profile_form = ProfileForm()

    if request.method == "POST":
        # check to see which form was saved

        if "first_name" in request.POST:

            # create form with user input
            user_update_form = UpdateUserForm(request.POST)

            # check if the form is valid
            if user_update_form.is_valid():
                # get the validated form inputs
                first_name_update = user_update_form.cleaned_data["first_name"]
                last_name_update = user_update_form.cleaned_data["last_name"]
                email_update = user_update_form.cleaned_data["email"]
                tel_number_update = user_update_form.cleaned_data["tel_number"]

                # update the user values
                user = request.user
                user.first_name = first_name_update
                user.last_name = last_name_update
                user.email = email_update
                user.tel_number = tel_number_update
                # save changes
                user.save()

                # redirect user to the same page
                return HttpResponsePermanentRedirect(reverse("account-settings"))
            else:
                print(user_update_form.errors)

        if "profile" in request.POST:
            # create profile form with submitted information

            # check if the user uploaded a new profile image
            if len(request.FILES.keys()) < 1:
                # no image uploaded, therefore use the same image on the database - not ideal because I am making a transaction with data already on the database
                request.FILES["profile_image"] = request.user.profile.profile_image

            # create a profile form with the saved correct profile image
            user_profile_form_submitted = ProfileForm(request.POST, request.FILES)

            # validate the inputs
            if user_profile_form_submitted.is_valid():
                # add user to the submitted form
                user_profile_form_submitted_valid = user_profile_form_submitted.save(
                    commit=False
                )
                user_profile_form_submitted_valid.user_id = request.user.id  # .username

                # add to profile table
                user_profile_form_submitted_valid.save()

                return HttpResponsePermanentRedirect(reverse("account-settings"))
            else:
                print(user_profile_form_submitted.errors)

    else:
        # create the form when someone lands on the page
        user_update_form = UpdateUserForm()
        # create the profile update form when user lands on the page
        user_profile_form = ProfileForm()

    # create context
    context = {
        "user_logged_in": user_logged_in,
        "user_update_form": user_update_form,
        "user_profile_form": user_profile_form,
    }

    return render(request, template_page, context)


def user_favourites(request):
    template_page = "drone_page/profile/favourites.html"
    context = {}
    return render(request, template_page, context)


def user_blocked(request):
    template_page = "drone_page/profile/blocked.html"
    context = {}
    return render(request, template_page, context)


def user_features(request):
    template_page = "drone_page/profile/features.html"
    context = {}
    return render(request, template_page, context)


class IndexView(TemplateView):
    # set template to be rendered
    template_name = "drone_page/index.html"

    # get context
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # define page context dictionary
        context = super().get_context_data(**kwargs)
        # get the reviews
        reviews = JobReviewModel.objects.all()
        # add reviews to context dictionary
        context["reviews"] = reviews
        # get the pilots
        pilots = Profile.objects.filter(user__user_type="Pilot")
        # add pilots to the context dictionary
        context["pilots"] = pilots
        return context


def browse_pilots(request):

    # browse_pilots page
    template_page = "drone_page/browse-pilots.html"

    # query users to get all pilots
    pilots = User.objects.filter(user_type="Pilot")

    context = {"pilots": pilots}

    return render(request, template_page, context)


def pilot_detail(request, slug):
    # slug format - username
    pilot = get_object_or_404(User, username=slug)

    # set template for pilot detail
    template_page = "drone_page/pilot-detail.html"

    # slug: first_name-userid-username

    # template context
    context = {"pilot": pilot}

    return render(request, template_page, context)


@method_decorator(login_required, name="dispatch")
class JobReview(CreateView):

    # set the template for this view
    template_name = "drone_page/job-review.html"
    # define the model used in this class
    model = JobReviewModel
    # set the form used in this view
    form_class = JobReviewForm

    # define success url
    success_url = "index"

    def get_form_kwargs(self) -> dict[str, Any]:
        return super().get_form_kwargs()

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form_obj = form.save(commit=False)

        if self.request.user != form_obj.review_job.request_pilot.user:
            form_obj.request_pilot = form_obj.review_job.request_pilot
            form_obj.save()
            return HttpResponsePermanentRedirect(reverse("index"))
        else:
            messages.error(self.request, "Pilot cannot self review")
            return super().form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # get view context and save as dictionary
        context = super().get_context_data(**kwargs)
        return context

    # pass


class JobRequest(CreateView):
    model = JobRequestModel
    form_class = JobRequestsForm
    template_name = "drone_page/job-request.html"
    success_url = "index"

    def form_valid(self, form):
        # save the form
        super().form_valid(form)
        return HttpResponsePermanentRedirect(reverse("index"))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["pilots"] = Profile.objects.filter(user__user_type="Pilot")
        context["countries"] = Country.objects.all()
        context["job_types"] = JobType.objects.all()
        return context


def load_cities(request):
    country_id = request.GET.get("country_id")
    cities = City.objects.filter(country_id=country_id)
    context = {"cities": cities}
    return render(
        request, "drone_page/profile/city_dropdown_list_options.html", context
    )


def load_job_request_cities(request):
    country_id = request.GET.get("request_country_id")
    cities = City.objects.filter(country_id=country_id)
    context = {"cities": cities}
    return render(
        request, "drone_page/profile/city_dropdown_list_options.html", context
    )


# def user_account_settings(request):
#     template_page = "drone_page/profile/account-settings.html"

#     pass
