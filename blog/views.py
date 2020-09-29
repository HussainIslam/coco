from django.views.generic import (  CreateView, 
                                    ListView, 
                                    DetailView, 
                                    UpdateView, 
                                    DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Blog
from .forms import BlogModelForm
from comments.forms import BlogCommentForm
from comments.models import BlogComment


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogModelForm
    login_url = 'account_login'
    template_name = 'Blog/create_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDetailView(LoginRequiredMixin, DetailView):
    login_url = 'account_login'
    template_name = 'Blog/detail_blog.html'

    def get_object(self):
        return get_object_or_404(Blog,id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        blog_object = self.get_object()
        kwargs['blog'] = blog_object
        kwargs["comments"] = BlogComment.objects.filter(blog=blog_object)
        if 'comment_form' not in kwargs:
            kwargs['comment_form'] = BlogCommentForm()
        return kwargs
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        context = {}
        if 'body' in request.POST:
            comment_form = BlogCommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = BlogComment()
                new_comment.blog = self.get_object()
                new_comment.commenter = self.request.user
                new_comment.body = comment_form.cleaned_data['body']
                new_comment.save()
                return HttpResponseRedirect(reverse_lazy('detail_blog', kwargs={'pk': self.get_object().id}))
            else:
                context['comment_form'] = comment_form
        return render(request, self.template_name, self.get_context_data(**context))
    
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