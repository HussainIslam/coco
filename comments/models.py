from django.db import models
from django.contrib.auth import get_user_model
from problems.models import Problem

class Comment(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by { self.commenter.username } on { self.problem.title }'