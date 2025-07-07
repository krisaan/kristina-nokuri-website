from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import BlogPostForm
from .forms import ContactForm

# Create your views here.


# Function-based view (example)
def hello_world(request):
    return HttpResponse("Hello, world!")


# Class-based view: requires inheritance
class HelloEthiopia(View):
    def get(self, request):
        return HttpResponse("Hello Ethiopia")


def home(request):
    if request.method == "GET":
        return render(request, "index.html")


def projects(request):
    if request.method == "GET":
        return render(request, "projects.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("Success")
    return render(request, "contact.html", {"form": form})
