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

    def test_course_list_view_url_exists_at_desired_location(self):
        """Test: test_course_list_view_url_exists_at_desired_location"""
        response = self.client.get('courses/')
        self.assertEqual(response.status_code, 200)

    def test_course_list_view_url_accessible_by_name(self):
        """Test: course list view url accessible by name"""
        response = self.client.get(reverse('courses:course-list'))
        self.assertEqual(response.status_code, 200)
