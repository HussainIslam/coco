from django.urls import path

from .views import HomePageView, MarkdownTutorialPageView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('markdown-tutorial/', MarkdownTutorialPageView, name="markdown_tutorial")
]
