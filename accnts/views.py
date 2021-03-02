from django.shortcuts import render, reverse
from django.views import generic

from courses.models import Course
from . import forms


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class ProfileView(generic.base.View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        course_count = Course.objects.filter(trainer=current_user).count()

        context = {
            'user_name': current_user.username,
            'course_count': course_count,
        }

        return render(request, 'registration/profile.html', context)
