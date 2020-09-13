from django.urls import path

from .views import ProblemCreateView, ProbelmDetailView

urlpatterns = [
    path('create/', ProblemCreateView.as_view(), name='create_problem'),
    path('<int:pk>/', ProbelmDetailView.as_view(), name="detail_problem"),
]
