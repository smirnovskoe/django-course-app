from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.views import generic

from . import forms
from . import models


class LandingPageView(generic.TemplateView):
    """Main page"""
    template_name = 'landing.html'


@login_required
def course_list(request):
    search_value = request.GET.get('search')
    current_user = request.user

    if search_value:
        courses = models.Course.objects.filter(
            Q(trainer=current_user) &
            Q(course_name__icontains=search_value)
        )
    else:
        courses = models.Course.objects.filter(trainer=current_user).order_by('-publish')
        for cr in courses:
            print(cr.status)

    context = {
        'courses': courses,
    }

    return render(request, 'courses/course_list.html', context)


def course_detail(request, slug):
    course = models.Course.objects.get(slug=slug)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)


def course_create(request):
    form = forms.CourseModelForm()

    if request.method == 'POST':
        form = forms.CourseModelForm(request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.trainer = request.user
            new_course.save()

            messages.success(request, 'Hellow')

            return redirect('courses:course-list')

    context = {
        'form': form,
        'course_id': 15,
    }

    return render(request, 'courses/course_create.html', context)


def course_update(request, slug):
    course = models.Course.objects.get(slug=slug)

    form = forms.CourseModelForm(instance=course)

    if request.method == 'POST':
        form = forms.CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()

            return redirect('/courses')

    context = {
        'form': form,
        'course': course,
    }

    return render(request, 'courses/course_update.html', context)


def course_delete(request, slug):
    course = models.Course.objects.get(slug=slug)
    course.delete()

    return redirect('/courses')


"""
def course_create(request):
    form = forms.CourseModelForm()

    if request.method == 'POST':
        form = forms.CourseModelForm(request.POST)
        if form.is_valid():
            # TODO: сделать привязку к текущему юзеру
            current_user = models.User.objects.first()
            # Создаем новый объект
            models.Course.objects.create(
                course_name=form.cleaned_data['course_name'],
                trainer=current_user,
                date_start=form.cleaned_data['date_start'],
                date_end=form.cleaned_data['date_end'],
            )
            return redirect('/courses')
    context = {
        'form': form,
    }
    return render(request, 'courses/course_create.html', context)
"""
