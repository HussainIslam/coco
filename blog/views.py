from django.views.generic import (  CreateView, 
                                    ListView, 
                                    DetailView, 
                                    UpdateView, 
                                    DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .models import Blog
from .forms import BlogModelForm


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogModelForm
    template_name = 'Blog/create_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'Blog/detail_blog.html'

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'Blog/list_blogs.html'

class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogModelForm
    template_name = 'Blog/update_blog.html'

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user

class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')
    template_name = 'Blog/delete_blog.html'

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user