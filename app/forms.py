# similar to inheriting models, just inherit from form class
from django import forms
from .models import BlogPost, ContactItem, ProjectItem


# we use ModelForm to link form to a model we made
class BlogPostForm(forms.ModelForm):
    # define some metadata
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "subtitle",
            "photo",
            "photo_alt"
        ]  # passes fields from BlogPost to form


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactItem
        fields = ["name", "email", "subject", "content"]

# allow project upload & edit from admin panel
class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields=[
            "title", 
            "subtitle",
            "description", 
            "photo",
            "photo_alt",
        ]