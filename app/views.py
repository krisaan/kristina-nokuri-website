from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from .forms import BlogPostForm
from .models import BlogPost
from .forms import ContactForm

import os
from dotenv import load_dotenv

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
    if request.method == "GET":
        blog_posts = BlogPost.objects.all()
        return render(request, "blog.html", {"blog_posts": blog_posts})


def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            content = form.cleaned_data["content"]

            full_message = (
                f"New contact form submission from personal website\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n"
                f"Message:\n{content}"
            )

            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[os.getenv("MY_EMAIL")],
            )
            return HttpResponse("Success")
    return render(request, "contact.html", {"form": form})
