from django.urls import path

from . import views

app_name = 'materials'

urlpatterns = [
    path('<int:lesson_id>', views.material_list, name='material-list'),
    path('upload/', views.material_upload, name='material-upload'),
]
