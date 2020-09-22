from django.urls import path

from .views import (BlogListView, 
                    BlogCreateView, 
                    BlogDetailView,
                    BlogUpdateView,
                    BlogDeleteView,)

urlpatterns = [
    path('', BlogListView.as_view(), name="blogs"),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail_blog"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update_blog"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
]
