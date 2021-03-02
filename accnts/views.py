from django.shortcuts import reverse
from django.views import generic

from . import forms


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')
