from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


from .forms import SignUpForm, LoginForm

User = get_user_model()
# Create your views here.


def index(request):

    # index_page
    template_page = "drone_page/index.html"
    context = {}

    return render(request, template_page, context)


def browse_pilots(request):

    # browse_pilots page
    template_page = "drone_page/browse-pilots.html"

    # query users to get all pilots
    pilots = User.objects.filter(user_type="Pilot")

    
    context = {"pilots": pilots}

    return render(request, template_page, context)


def job_review(request):
    template_page = "drone_page/job-review.html"
    context = {}

    return render(request, template_page, context)


def job_request(request):
    template_page = "drone_page/job-request.html"
    context = {}

    return render(request, template_page, context)


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


@login_required(login_url="login")
def user_dashboard(request):
    template_page = "drone_page/profile/dashboard.html"
    context = {}
    return render(request, template_page, context)


def user_settings(request):
    template_page = "drone_page/profile/account-settings.html"
    context = {}
    return render(request, template_page, context)


def user_favourites(request):
    template_page = "drone_page/profile/favourites.html"
    context = {}
    return render(request, template_page, context)


def user_blocked(request):
    template_page = "drone_page/profile/blocked.html"
    context = {}
    return render(request, template_page, context)


def user_logout(request):

    auth.logout(request)

    request.session.flush()
    "... request"

    return HttpResponsePermanentRedirect(reverse("index"))


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
            print("not valid?")
            print(form.errors)
            messages.add_message(request, messages.ERROR, form.errors)
            return HttpResponseRedirect(reverse("sign-up"))
    else:
        # create form when someone lands on the page
        form = SignUpForm()

    context = {"form": form}

    return render(request, template_page, context)
