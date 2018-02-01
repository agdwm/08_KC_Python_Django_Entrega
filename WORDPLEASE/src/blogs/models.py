import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

    class Meta:
        abstract = True


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    # Returns the representation of an object as a string.
    # It's very useful for working with the Django Admin Panel
    def __str__(self):
        return self.name


class Blog(TimeStampedModel):

    blog_title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_title


class Post(TimeStampedModel):

    post_title = models.CharField(max_length=150)
    intro = models.CharField(max_length=400)
    content = models.TextField()
    video = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    release_date = models.DateTimeField()

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.post_title
