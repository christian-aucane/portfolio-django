from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.translation import gettext as _

from .models import SiteMetaData, FontAwesomeIcon, FooterCredits, Favicon


class SiteMetaDataTestCase(TestCase):
    def test_update_default_entry(self):
        default_entry = SiteMetaData.objects.first()

        new_title = "New Site Title"
        new_description = "New Site Description"
        new_author = "New Author"
        default_entry.title = new_title
        default_entry.description = new_description
        default_entry.author = new_author
        default_entry.save()

        updated_entry = SiteMetaData.objects.get(title=new_title)
        self.assertIsNotNone(updated_entry)
        self.assertEqual(updated_entry.description, new_description)
        self.assertEqual(updated_entry.author, new_author)

    def test_cannot_create_additional_entries(self):
        with self.assertRaises(ValidationError):
            new_entry = SiteMetaData.objects.create(
                title="Another Site Title",
                description="Another Site Description",
                author="Another Author"
            )

class FooterCreditsTestCase(TestCase):

    def test_template_credits_read_only(self):
        template_credits = FooterCredits.objects.get(pk=1)

        self.assertEqual(str(template_credits), "Template Credits (Read Only)")

        template_credits.title = "New Title"
        template_credits.save()
        self.assertEqual(template_credits.title, _("Template credits"))

        with self.assertRaises(ValidationError):
            template_credits.delete()

    def test_create_and_delete_other_credits(self):
        new_credits = FooterCredits.objects.create(
            title="New Credits",
            html="<p>New HTML Content</p>"
        )

        self.assertEqual(str(new_credits), "New Credits")

        new_credits.delete()

        with self.assertRaises(FooterCredits.DoesNotExist):
            FooterCredits.objects.get(pk=new_credits.pk)


class FaviconTestCase(TestCase):

    def setUp(self):
        self.favicon = Favicon.objects.first()

    def test_favicon_read_only(self):
        self.assertEqual(str(self.favicon), "Favicon")
        with self.assertRaises(ValidationError):
            self.favicon.delete()

    def test_edit_favicon(self):
        self.assertEqual(str(self.favicon), "Favicon")
        self.favicon.credits_html = "<p>Updated Favicon Credits</p>"
        self.favicon.save()
        self.assertEqual(self.favicon.credits_html, "<p>Updated Favicon Credits</p>")

    def test_unique_favicon_instance(self):
        with self.assertRaises(ValidationError):
            Favicon.objects.create(
                image=None,
                credits_html="<p>Another Favicon Credits</p>"
            )


class FontAwesomeIconTests(TestCase):
    def setUp(self):
        self.icon = FontAwesomeIcon.objects.create(
            title="Test Icon",
            css_classes="fa fa-test"
        )

    def test_icon_creation(self):
        self.assertEqual(self.icon.title, "Test Icon")
        self.assertEqual(self.icon.css_classes, "fa fa-test")

    def test_icon_str(self):
        self.assertEqual(str(self.icon), "Test Icon")
