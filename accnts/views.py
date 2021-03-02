from django.shortcuts import render, reverse
from django.views import generic

from . import forms


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class ProfileView(generic.base.View):
    def get(self, request, *args, **kwargs):
        current_user = request.user

        context = {
            'user_name': current_user.username
        }

        return render(request, 'registration/profile.html', context)
