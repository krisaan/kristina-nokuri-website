from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    created_at = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="blog_photos/")

    def __str__(self):
        return self.title


class ContactItem(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
