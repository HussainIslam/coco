from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

from taggit.managers import TaggableManager

class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    cover = models.ImageField(null=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="draft")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')
    blog_tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_blog", kwargs={"pk": self.pk})
    