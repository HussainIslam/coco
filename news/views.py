from django.shortcuts import render
from django.views.generic import ListView

from .models import News

class NewsListView(ListView):
    template_name = 'News/list_news.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return News.objects.all()