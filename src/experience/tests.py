from django.conf import settings
from django.test import TestCase
from .models import Experience
from datetime import date


class ExperienceTestCase(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Software Engineer",
            company="ABC Inc",
            description="Worked on various projects.",
            start_date=date(2022, 1, 1),
            end_date=date(2023, 1, 1),
            thumbnail="path/to/image_thumbnail.jpg"
        )

    def test_experience_creation(self):
        self.assertEqual(str(self.experience), "Software Engineer at ABC Inc")

    def test_experience_dates(self):
        self.assertEqual(self.experience.start_date, date(2022, 1, 1))
        self.assertEqual(self.experience.end_date, date(2023, 1, 1))

    def test_experience_search(self):
        result = Experience.objects.filter(title="Software Engineer")
        self.assertEqual(result.count(), 1)
        self.assertEqual(result[0], self.experience)

    def test_experience_thumbnail_url(self):
        expected_url = settings.MEDIA_URL + "path/to/image_thumbnail.jpg"
        self.assertEqual(self.experience.get_thumbnail_url(), expected_url)
