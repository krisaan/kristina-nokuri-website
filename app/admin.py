from django.contrib import admin
from .models import BlogPost, ContactItem, ProjectItem

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(ContactItem)
admin.site.register(ProjectItem)
