from django.db import models
from account.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=False, null=True)
    text = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=False, null=True)
    post_reference = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
    text = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    description = models.TextField(max_length=500, blank=True)
    image_profile = models.ImageField(upload_to='images', blank=True, null=True)
    followers = models.ManyToManyField(CustomUser, related_name='followers', blank=True)
