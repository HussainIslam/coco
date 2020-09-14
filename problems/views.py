from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from taggit.models import Tag

from .models import Problem
from .forms import ProblemModelForm

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
    model = Problem
    template_name = 'Problems/detail_problem.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs)
        problem_id = self.kwargs.get("pk")
        context = super(ProbelmDetailView, self).get_context_data(**kwargs)
        context["problem"] = get_object_or_404(Problem, id=problem_id)
        return context

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Problem, id=id_)
    

class ProblemUpdateView(UpdateView):
    model = Problem
    form_class = ProblemModelForm
    template_name = 'Problems/update_problem.html'