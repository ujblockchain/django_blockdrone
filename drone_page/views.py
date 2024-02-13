from django.shortcuts import render

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
    template_page = "drone_page/accounts/sign_up.html"
    context = {}

    return render(request, template_page, context)