from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    # Si el usuario se elimina de la BBDD se eliminarán también los blogs de dicho usuario.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title


class Post(models.Model):
    post_title = models.CharField(max_length=50)
    headline = models.TextField(max_length=100)
    content = models.TextField()
    media = models.URLField(blank=True, null=True)
    release_date = models.DateTimeField()

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title



