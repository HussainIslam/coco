from django.urls import path

from .views import ProblemListView, ProblemCreateView, ProbelmDetailView, ProblemUpdateView, ProblemDeleteView, TaggedItemListView

urlpatterns = [
    path('', ProblemListView.as_view(), name='list_problems'),
    path('create/', ProblemCreateView.as_view(), name='create_problem'),
    path('<int:pk>/', ProbelmDetailView.as_view(), name="detail_problem"),
    path('<int:pk>/update/', ProblemUpdateView.as_view(), name="update_problem"),
    path('<int:pk>/delete/', ProblemDeleteView.as_view(), name="delete_problem"),
    path('tag/<slug:slug>/', TaggedItemListView.as_view(),name="same_tag"),
]
