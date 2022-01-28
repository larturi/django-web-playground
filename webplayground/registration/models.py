from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='ptofiles', blank=True, null=True),
    bio = models.TextField(blank=True, null=True),
    link = models.URLField(max_length=200, blank=True, null=True)
