from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from problems.models import Problem
from .models import Comment

class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'Comments/delete_comment.html'
    
    def get_success_url(self, **kwargs):
        problem_id = self.kwargs['pk']
        cur_problem = Comment.objects.get(id=problem_id).problem
        return reverse_lazy('detail_problem', kwargs={'pk': cur_problem.id})