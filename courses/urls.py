from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('create/', views.course_create, name='course-create'),
    path('<slug:slug>', views.course_detail, name='course-detail'),
    path('<slug:slug>/update/', views.course_update, name='course-update'),
    path('<slug:slug>/delete/', views.course_delete, name='course-delete'),

]
