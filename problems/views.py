from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Problem
from .forms import ProblemModelForm

class ProblemCreateView(CreateView):
    model = Problem
    form_class = ProblemModelForm
    template_name = 'Problems/create_problem.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProbelmDetailView(DetailView):
    model = Problem
    template_name = 'Problems/detail_problem.html'
