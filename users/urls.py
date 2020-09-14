from django.urls import path

from .views import (SignupView,
                    ProfileView,
                    ProgrammingLanguageCreate, 
                    ProgrammingLanguageDetailView, 
                    ProgrammingLanguageListView,
                    ProgrammingLanguageUpdateView,
                    ProgrammingLanguageDeleteView)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('languages/', ProgrammingLanguageListView.as_view(), name='languages'),
    path('languages/add/', ProgrammingLanguageCreate.as_view(), name='create_pl'),
    path('languages/<int:pk>/', ProgrammingLanguageDetailView.as_view(), name='detail_pl'),
    path('languages/<int:pk>/update/', ProgrammingLanguageUpdateView.as_view(), name='update_pl'),
    path('languages/<int:pk>/delete/', ProgrammingLanguageDeleteView.as_view(), name='delete_pl'),
]
