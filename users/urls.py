from django.urls import path

from .views import (SignupView, 
                    ProgrammingLanguageCreate, 
                    ProgrammingLanguageDetailView, 
                    ProgrammingLanguageListView,
                    ProgrammingLanguageUpdateView)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('languages/', ProgrammingLanguageListView.as_view(), name='languages'),
    path('languages/add/', ProgrammingLanguageCreate.as_view(), name='create_pl'),
    path('languages/<int:pk>/', ProgrammingLanguageDetailView.as_view(), name='detail_pl'),
    path('languages/<int:pk>/update/', ProgrammingLanguageUpdateView.as_view(), name='update_pl'),
]
