from django.db import models
from PIL import Image


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    created_at = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="blog_photos/")
    photo_alt = models.CharField(
        max_length=255, default="Blog photo image.", blank=False
    )

    def __str__(self):
        return self.title


class ContactItem(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class ProjectItem(models.Model):
    repo_id = models.PositiveBigIntegerField(unique=True, default=0)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="project_media/")
    photo_alt = models.CharField(max_length=255, default="Project image.")
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title