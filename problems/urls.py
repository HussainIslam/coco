from django.urls import path

from .views import ProblemCreateView

urlpatterns = [
    path('create/', ProblemCreateView.as_view(), name='create_problem'),
]
