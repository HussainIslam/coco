from django.urls import path

from .views import BlogListView, BlogCreateView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name="blogs"),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail_blog"),
]
