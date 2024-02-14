from django.shortcuts import render
from . forms import SignUpForm
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
        form = SignUpForm(request.Post)
        # validate the inpits
        if form.is_valid():
             pass
        # redirect to login page
    
    # create form when someone lands on the page
    form = SignUpForm()
    context = {}

    return render(request, template_page, context)
