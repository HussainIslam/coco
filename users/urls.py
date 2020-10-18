from django.urls import path

from .views import (SignupView,
                    UserLoginView,
                    ProfileView,
                    OtherProfileDetailView,
                    ProfileUpdateView,
                    ProgrammingLanguageCreate, 
                    ProgrammingLanguageDetailView, 
                    ProgrammingLanguageListView,
                    ProgrammingLanguageUpdateView,
                    ProgrammingLanguageDeleteView)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', OtherProfileDetailView.as_view(), name="user_profile"),
    path('profile/update/', ProfileUpdateView.as_view(), name="profile_update"),
    path('languages/', ProgrammingLanguageListView.as_view(), name='languages'),
    path('languages/add/', ProgrammingLanguageCreate.as_view(), name='create_pl'),
    path('languages/<int:pk>/', ProgrammingLanguageDetailView.as_view(), name='detail_pl'),
    path('languages/<int:pk>/update/', ProgrammingLanguageUpdateView.as_view(), name='update_pl'),
    path('languages/<int:pk>/delete/', ProgrammingLanguageDeleteView.as_view(), name='delete_pl'),
]
