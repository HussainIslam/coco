from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Blog
from .forms import BlogModelForm

class BlogCreateView(CreateView):
    form_class = BlogModelForm
    template_name = 'Blog/create_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'Blog/detail_blog.html'

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'Blog/list_blogs.html'

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogModelForm
    context_object_name = 'blog'
    template_name = 'Blog/update_blog.html'