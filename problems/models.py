from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager

from users.models import ProgrammingLanguage

class Problem(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    code = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES, default="easy")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='problems')
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.SET_NULL, related_name='problems', null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_problem", kwargs={"pk": self.pk})
    