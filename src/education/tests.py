from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from .models import Education


class EducationTestCase(TestCase):
    def setUp(self):
        self.education_data = {
            'school_name': 'Wild Code School',
            'program': 'Data - Intelligence Artificielle',
            'role': 'Développeur en Intelligence Artificielle',
            'description': 'Major de promotion',
            'thumbnail': SimpleUploadedFile("thumbnail.jpg", b"file_content", content_type="image/jpeg"),
            'start_date': timezone.now(),
            'end_date': timezone.now(),
        }

    def test_education_creation(self):
        education = Education.objects.create(**self.education_data)
        self.assertEqual(str(education), f"{self.education_data['school_name']} - {self.education_data['program']}")
        self.assertEqual(education.get_duration(), f"{self.education_data['start_date'].strftime('%b %Y')} - {self.education_data['end_date'].strftime('%b %Y')}")

    def test_education_str_method(self):
        education = Education.objects.create(**self.education_data)
        expected_str = f"{self.education_data['school_name']} - {self.education_data['program']}"
        self.assertEqual(str(education), expected_str)

    def test_education_duration_method(self):
        education = Education.objects.create(**self.education_data)
        expected_duration = f"{self.education_data['start_date'].strftime('%b %Y')} - {self.education_data['end_date'].strftime('%b %Y')}"
        self.assertEqual(education.get_duration(), expected_duration)
