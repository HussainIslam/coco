from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin

from problems.models import Problem
from .models import Comment
from .forms import CommentForm

class CustomCommentMixin(object):
    def get_success_url(self, **kwargs):
        problem_id = self.kwargs['pk']
        cur_problem = Comment.objects.get(id=problem_id).problem
        return reverse_lazy('detail_problem', kwargs={'pk': cur_problem.id})

    def test_func(self):
        comment = self.get_object()
        return comment.commenter == self.request.user

class DeleteCommentView(CustomCommentMixin,DeleteView):
    model = Comment
    template_name = 'Comments/delete_comment.html'
    
    

class CommentUpdateView(CustomCommentMixin,UpdateView):
    form_class = CommentForm
    template_name = 'Comments/update_comment.html'

    def get_object(self, **kwargs):
        return Comment.objects.get(id=self.kwargs['pk'])

