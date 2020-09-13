from django.urls import path

from .views import ProblemCreateView, ProbelmDetailView, ProblemUpdateView

urlpatterns = [
    path('create/', ProblemCreateView.as_view(), name='create_problem'),
    path('<int:pk>/', ProbelmDetailView.as_view(), name="detail_problem"),
    path('<int:pk>/update/', ProblemUpdateView.as_view(), name="update_problem"),
]
