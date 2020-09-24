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
    login_url = 'account_login'
    template_name = 'Blog/create_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'blog'
    login_url = 'account_login'
    template_name = 'Blog/detail_blog.html'

    def get_object(self):
        obj = Blog.objects.get(id=self.kwargs['pk'])
        print(obj.cover)
        return obj

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    login_url = 'account_login'
    context_object_name = 'blogs'
    template_name = 'Blog/list_blogs.html'

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogModelForm
    login_url = 'account_login'
    template_name = 'Blog/update_blog.html'

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')
    login_url = 'account_login'
    template_name = 'Blog/delete_blog.html'

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user