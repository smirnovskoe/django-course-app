from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse, render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.utils.safestring import mark_safe

from . import forms
from . import models


# TODO: сделать календарь из стандартного модуля
class CalendarView(LoginRequiredMixin, generic.ListView):
    model = models.Lesson
    template_name = 'lessons/calendar.html'
    context_object_name = 'lessons'

    def get_queryset(self):
        return models.Lesson.objects.all()


def plan_view(request, lesson_id, course_id):
    lesson = models.Lesson.objects.get(id=lesson_id)
    plan = models.Plan.objects.get(lesson_id=lesson_id)

    form = forms.PlanModelForm(instance=plan)

    if request.method == 'POST':
        form = forms.PlanModelForm(request.POST or None, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('lessons:lesson-list', course_id)
        else:
            print(form.errors)

    context = {
        'lesson': lesson,
        'form': form,
    }

    return render(request, 'lessons/lesson_plan.html', context)


class LessonsListView(LoginRequiredMixin, generic.ListView):
    model = models.Lesson
    template_name = 'lessons/lesson_list.html'
    context_object_name = 'lessons'

    def get_queryset(self):
        print(self.kwargs)
        return models.Lesson.objects.filter(course_id=self.kwargs['course_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_name = models.Course.objects.get(id=self.kwargs['course_id'])
        context['course_name'] = course_name
        context['course_id'] = self.kwargs['course_id']
        return context


class LessonCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'lessons/lesson_create.html'
    form_class = forms.LessonModelForm
    success_message = "Lesson was created."

    def get_success_url(self, **kwargs):
        return redirect('lessons:lesson-list', kwargs['course_id'])

    def form_valid(self, form):
        new_lesson = form.save(commit=False)
        new_lesson.course_id = self.kwargs['course_id']
        new_lesson.save()

        return redirect('lessons:lesson-list', self.kwargs['course_id'])


class LessonDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'lessons/lesson_detail.html'
    context_object_name = 'lesson'

    def get_queryset(self):
        return models.Lesson.objects.all()


class LessonUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'lessons/lesson_update.html'
    form_class = forms.LessonModelForm

    def get_success_url(self):
        lesson = models.Lesson.objects.get(id=self.kwargs['pk'])
        return reverse('lessons:lesson-list', args=[lesson.course.id])

    def get_queryset(self):
        return models.Lesson.objects.all()


class LessonDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'lessons/lesson_delete.html'
    context_object_name = 'lesson'

    def get_success_url(self):
        return reverse('lessons:lesson-list', args=[self.kwargs['pk']])

    def get_queryset(self):
        return models.Lesson.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_id'] = self.kwargs['pk']
        return context
