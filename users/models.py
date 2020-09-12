from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    profile = models.TextField()
    dob = models.DateField(blank=True, null=True)

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=25)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name