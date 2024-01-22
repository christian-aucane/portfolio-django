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

    def test_icon_html(self):
        expected_html = '<i class="fa fa-test" title=Test Icon></i>'
        self.assertEqual(self.icon.html(), expected_html)

    def test_icon_li_html(self):
        expected_li_html = '<li><i class="fa-li fa fa-test" title=Test Icon></i></li>'
        self.assertEqual(self.icon.li_html(), expected_li_html)
