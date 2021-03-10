from django.urls import path

from . import views

app_name = 'lessons'

urlpatterns = [
    path('<int:course_id>', views.LessonsListView.as_view(), name='lesson-list'),
    path('create/<int:course_id>', views.LessonCreateView.as_view(), name='lesson-create'),
    path('<int:pk>', views.LessonDetailView.as_view(), name='lesson-detail'),
    path('<int:pk>/update/', views.LessonUpdateView.as_view(), name='lesson-update'),
    path('<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson-delete'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    # Function Based Views
    path('plan/lesson/<int:lesson_id>/course/<int:course_id>', views.plan_view, name='plan-view'),

]
