from django.urls import path
from . import views

# url mapping needs to occur at...
# 1: app level (here)
# 2: project level (project/urls.py) to link app
urlpatterns = [
    # path (address, view)
    path("function", views.hello_world),
    path(
        "class", views.HelloEthiopia.as_view()
    ),  # when passing in classes, need to add as_view()
    path("", views.home),
    path("blog", views.blog),
    path("contact", views.contact),
    path("projects", views.projects),
]
