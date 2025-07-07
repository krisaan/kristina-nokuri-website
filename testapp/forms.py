# similar to inheriting models, just inherit from form class
from django import forms
from .models import BlogPost
from .models import ContactItem


# we use ModelForm to link form to a model we made
class BlogPostForm(forms.ModelForm):
    # define some metadata
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "subtitle",
            "photo",
        ]  # passes fields from BlogPost to form


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactItem
        fields = ["name", "email", "subject", "content"]
