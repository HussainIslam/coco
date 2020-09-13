from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Problem

class ProblemCreateView(CreateView):
    model = Problem
    fields = ('title', 'language', 'body',)
    template_name = 'Problems/create_problem.html'