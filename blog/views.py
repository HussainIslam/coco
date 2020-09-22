from django.views.generic import CreateView, ListView, DetailView

from .models import Blog
from .forms import BlogModelForm

class BlogCreateView(CreateView):
    form_class = BlogModelForm
    context_object_name = 'blog'
    template_name = 'Blog/create_blog.html'