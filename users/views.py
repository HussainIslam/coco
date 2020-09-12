from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, ProgrammingLanguageForm
from .models import ProgrammingLanguage

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

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