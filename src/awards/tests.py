from django.conf import settings
from django.test import TestCase
from .models import AwardCategory, Award


class AwardCategoryModelTests(TestCase):
    def test_award_category_creation(self):
        award_category = AwardCategory.objects.create(
            title="Programming",
            icon="fa-code",
            icon_color="blue"
        )

        self.assertEqual(award_category.title, "Programming")
        self.assertEqual(award_category.icon, "fa-code")
        self.assertEqual(award_category.icon_color, "blue")
        self.assertEqual(str(award_category), "Programming")

    def test_award_category_display_order(self):
        award_category_1 = AwardCategory.objects.create(
            title="Programming",
            icon="fa-code",
            icon_color="blue"
        )
        award_category_2 = AwardCategory.objects.create(
            title="Design",
            icon="fa-paint-brush",
            icon_color="red"
        )

        self.assertEqual(award_category_1.display_order, 1)
        self.assertEqual(award_category_2.display_order, 2)


class AwardModelTests(TestCase):
    def setUp(self):
        self.award_category = AwardCategory.objects.create(
            title="Programming",
            icon="fa-code",
            icon_color="blue"
        )

    def test_award_creation(self):
        award = Award.objects.create(
            title="Python Certification",
            text="Achieved Python certification with honors.",
            category=self.award_category
        )

        self.assertEqual(award.title, "Python Certification")
        self.assertEqual(award.text, "Achieved Python certification with honors.")
        self.assertEqual(award.category, self.award_category)
        self.assertEqual(str(award), "Python Certification (Programming)")
        self.assertEqual(award.display_order, 1)

    def test_award_file_url(self):
        award = Award.objects.create(
            title="JavaScript Certification",
            text="Completed advanced JavaScript course.",
            file="path/to/file.pdf",
            category=self.award_category
        )

        expected_url = settings.MEDIA_URL + "path/to/file.pdf"
        self.assertEqual(award.get_file_url(), expected_url)
