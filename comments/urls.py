from django.urls import path

from .views import DeleteCommentView, CommentUpdateView

urlpatterns = [
    path('<int:pk>/delete/', DeleteCommentView.as_view(), name="delete_comment"),
    path('<int:pk>/update/', CommentUpdateView.as_view(), name="update_comment"),
]
