from django.shortcuts import render, redirect

from . import forms
from . import models


def material_list(request, lesson_id):
    materials = models.Material.objects.filter(lesson__id=lesson_id)

    context = {
        'materials': materials
    }

    print(materials)

    return render(request, 'materials/material_list.html', context)


def material_upload(request):
    form = forms.MaterialModelForm()
    if request.method == 'POST':
        form = forms.MaterialModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses:course-list')

    context = {
        'form': form,
    }

    return render(request, 'materials/material_upload.html', context)
