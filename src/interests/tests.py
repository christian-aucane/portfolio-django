from django.db import IntegrityError
from django.test import TestCase

from .models import Paragraph


class ParagraphModelTests(TestCase):
    def test_paragraph_creation(self):
        paragraph = Paragraph.objects.create(
            title="Introduction",
            text="This is a test paragraph."
        )
        self.assertEqual(str(paragraph), "Introduction - Paragraph 1")

    def test_paragraph_unique_title(self):
        with self.assertRaises(IntegrityError):
            Paragraph.objects.create(title="Unique Title", text="Some text.")
            Paragraph.objects.create(title="Unique Title", text="Different text.")

    def test_paragraph_display_order_auto_increment(self):
        paragraph1 = Paragraph.objects.create(title="Auto Increment 1", text="Text 1")
        paragraph2 = Paragraph.objects.create(title="Auto Increment 2", text="Text 2")
        self.assertEqual(paragraph1.display_order, 1)
        self.assertEqual(paragraph2.display_order, 2)
