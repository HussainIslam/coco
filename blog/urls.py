from django.urls import path

from .views import BlogCreateView, BlogDetailView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail_blog"),
]
