from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    # Returns the representation of an object as a string.
    # It's very useful for working with the Django Admin Panel
    def __str__(self):
        return self.name


class Blog(models.Model):

    blog_title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title


class Post(models.Model):

    post_title = models.CharField(max_length=50)
    headline = models.CharField(max_length=100)
    content = models.TextField()
    media = models.URLField(blank=True, null=True)
    release_date = models.DateTimeField()

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

    def __str__(self):
        return self.post_title



