from django.test import TestCase
from .models import FontAwesomeIcon

class FontAwesomeIconTests(TestCase):
    def setUp(self):
        self.icon = FontAwesomeIcon.objects.create(
            title="Test Icon",
            classes="fa fa-test"
        )

    def test_icon_creation(self):
        self.assertEqual(self.icon.title, "Test Icon")
        self.assertEqual(self.icon.classes, "fa fa-test")

    def test_icon_str(self):
        self.assertEqual(str(self.icon), "Test Icon")
