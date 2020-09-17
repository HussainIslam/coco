from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, ProgrammingLanguageForm, CustomUserChangeForm
from .models import ProgrammingLanguage

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'users/current_profile.html'

    def get_object(self):
        return get_user_model().objects.get(username=self.request.user)

class ProfileUpdateView(UpdateView):
    form_class = CustomUserChangeForm
    context_object_name = 'user'
    template_name = 'users/update_profile.html'

    def get_object(self, queryset=None):
        return get_user_model().objects.get(username=self.request.user)

class ProgrammingLanguageListView(ListView):
    model = ProgrammingLanguage
    context_object_name = 'languages'
    template_name = 'ProgrammingLanguage/list_pl.html'

class ProgrammingLanguageDetailView(DetailView):
    model = ProgrammingLanguage
    context_object_name = 'language'
    template_name = 'ProgrammingLanguage/detail_pl.html'

class ProgrammingLanguageCreate(CreateView):
    form_class = ProgrammingLanguageForm
    template_name = 'ProgrammingLanguage/create_pl.html'

class ProgrammingLanguageUpdateView(UpdateView):
    model = ProgrammingLanguage
    form_class = ProgrammingLanguageForm
    context_object_name = 'language'
    success_url = reverse_lazy('languages')
    template_name = 'ProgrammingLanguage/update_pl.html'

class ProgrammingLanguageDeleteView(DeleteView):
    model = ProgrammingLanguage
    success_url = reverse_lazy('languages')
    context_object_name = 'language'
    template_name = 'ProgrammingLanguage/delete_pl.html'