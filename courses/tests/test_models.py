from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from courses.models import Course

User = get_user_model()


class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Run once to set up non-modified data for all class methods(tests)"""
        user = User.objects.create_user(username='test_user', password='12345')

        Course.objects.create(
            course_name='Python Course',
            description='Test description' * 10,
            trainer=user,
            date_start=datetime.strptime('2021-02-20', '%Y-%m-%d').date(),
            date_end=datetime.strptime('2021-03-03', '%Y-%m-%d').date(),
            status=Course.CourseStatus.DIDNT_START,
        )

    def setUp(self):
        """Run once for every test method to setup clean data"""
        ...

    def test_course_name_label(self):
        """Test: course_name label"""
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('course_name').verbose_name
        self.assertEquals(field_label, 'course name')

    def test_course_name_max_length(self):
        """Test: course_name max len"""
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('course_name').max_length
        self.assertEquals(max_length, 255)

    def test_course_string_representation(self):
        """Test: course_name string representation"""
        course = Course.objects.get(id=1)
        self.assertEquals(str(course), course.course_name)

    def test_course_name_plural(self):
        """Test: course_name plural"""
        self.assertEquals(Course._meta.verbose_name_plural, 'Courses')
