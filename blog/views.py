from django.views.generic import CreateView, ListView, DetailView

from .models import Blog

class BlogCreateView(CreateView):
    model_ = Blog
    context_object_name = 'blog'
    template_name = 'Blog/create_blog.html'