from django.db import models
from django.contrib.auth.models import User


class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()


