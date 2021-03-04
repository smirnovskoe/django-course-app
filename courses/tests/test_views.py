from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from courses.models import Course

User = get_user_model()


class CourseListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 10 courses
        number_of_courses = 10

        user = User.objects.create_user(username='test_user', password='12345')

        for idx in range(number_of_courses):
            Course.objects.create(
                course_name=f'Python Course Test {idx}',
                description='Test description' * idx,
                trainer=user,
                date_start=datetime.strptime('2021-02-20', '%Y-%m-%d').date(),
                date_end=datetime.strptime('2021-03-03', '%Y-%m-%d').date(),
                status=Course.CourseStatus.DIDNT_START,
            )

    def test_course_list_view_status_code(self):
        """Test: test course list view status code"""
        self.client.login(username='test_user', password='12345')
        response = self.client.get(reverse('courses:course-list'))
        self.assertEqual(response.status_code, 200)

    def test_course_list_view_template_name(self):
        """Test: test course list view template name"""
        self.client.login(username='test_user', password='12345')
        response = self.client.get(reverse('courses:course-list'))
        self.assertTemplateUsed(response, template_name='courses/course_list.html')

    def test_course_list_view_url_exists_at_desired_location(self):
        """Test: test course list view url exists at desired location"""
        self.client.login(username='test_user', password='12345')
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)

    def test_course_list_view_url_accessible_by_name(self):
        """Test: course list view url accessible by name"""
        self.client.login(username='test_user', password='12345')
        response = self.client.get(reverse('courses:course-list'))
        self.assertEqual(response.status_code, 200)
