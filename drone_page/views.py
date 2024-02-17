from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import SignUpForm

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
    context = {}

    return render(request, template_page, context)


def job_review(request):
    template_page = "drone_page/job-review.html"
    context = {}

    return render(request, template_page, context)


def job_request(request):
    template_page = "drone_page/job-request.html"
    context = {}

    return render(request, template_page, context)


def login(request):
    template_page = "drone_page/accounts/login.html"
    context = {}

    return render(request, template_page, context)


def logout(request):
    template_page = "drone_page/accounts/logout.html"
    context = {}

    return render(request, template_page, context)


def sign_up(request):

    template_page = "drone_page/accounts/signup.html"

    if request.method == "POST":
        # get the user inputs
        form = SignUpForm(request.POST)
        # validate the inpits
        if form.is_valid():

            user = User(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                user_type=form.cleaned_data["user_type"],
                tel_number=form.cleaned_data["tel_number"],
                password1=form.cleaned_data["password1"],
                password2=form.cleaned_data["password2"],
            )
            # save to database
            user.save()

            # redirect to login page
            login_path = reverse("login")
            return HttpResponseRedirect(login_path)
        else:
            print(form)
            print("not valid")

    # create form when someone lands on the page
    form = SignUpForm()
    context = {"form": form}

    return render(request, template_page, context)
