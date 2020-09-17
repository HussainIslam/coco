from django.urls import path

from .views import DeleteCommentView

urlpatterns = [
    path('<int:pk>/delete/', DeleteCommentView.as_view(), name="delete_comment"),
]
