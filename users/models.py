from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    profile = models.TextField()
    dob = models.DateField(blank=True, null=True)
    languages = models.ManyToManyField(
        to='users.ProgrammingLanguage',
        related_name='user_profile'
    )

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=25, unique=True)
    abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_pl", kwargs={"pk": self.pk})
    