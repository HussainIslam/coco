from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from taggit.models import Tag

from .models import Problem
from .forms import ProblemModelForm
from comments.models import Comment
from comments.forms import CommentForm

class ProblemListView(ListView):
    model = Problem
    context_object_name = 'problems'
    template_name = 'Problems/list_problems.html'

class ProblemCreateView(CreateView):
    form_class = ProblemModelForm
    template_name = 'Problems/create_problem.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProbelmDetailView(DetailView):
    template_name = 'Problems/detail_problem.html'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Problem, id=id_)
    
    def get_context_data(self, **kwargs):
        problem_object = self.get_object()
        kwargs['problem'] = problem_object
        kwargs['comments'] = Comment.objects.filter(problem=problem_object)
        if 'comment_form' not in kwargs:
            kwargs['comment_form'] = CommentForm()
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        ctxt = {}
        if 'body' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = Comment()
                new_comment.problem = self.get_object()
                new_comment.commenter = self.request.user
                new_comment.body = comment_form.cleaned_data['body']
                new_comment.save()
                return HttpResponseRedirect(reverse_lazy('detail_problem', kwargs={'pk': self.get_object().id}))
            else:
                ctxt['comment_form'] = comment_form
        return render(request, self.template_name, self.get_context_data(**ctxt))
    


class ProblemUpdateView(UpdateView):
    model = Problem
    form_class = ProblemModelForm
    template_name = 'Problems/update_problem.html'

class ProblemDeleteView(DeleteView):
    model = Problem
    success_url = reverse_lazy('list_problems')
    template_name = 'Problems/delete_problem.html'

class TaggedItemListView(ListView):
    context_object_name = 'problems'
    template_name = 'Problems/list_problems.html'

    def get_queryset(self):
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        problems = Problem.objects.filter(tags__name=tag)
        return problems

    def get_context_data(self, **kwargs):
        context = super(TaggedItemListView, self).get_context_data(**kwargs)
        context["tag"] = Tag.objects.get(slug=self.kwargs['slug'])
        return context
    