from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from .models import AboutInfo, AboutSkill, SocialLink


class AboutModelTests(TestCase):
    def setUp(self):
        self.about_info = AboutInfo.objects.create(
            first_name="John",
            last_name="Doe",
            description="A test description."
        )

    def test_about_info_creation(self):
        self.assertEqual(str(self.about_info), "About me")

    def test_about_info_save(self):
        with self.assertRaises(ValidationError):
            about_info_duplicate = AboutInfo(
                first_name="Jane",
                last_name="Doe",
                description="Another test description."
            )
            about_info_duplicate.save()

    def test_about_info_delete(self):
        with self.assertRaises(ValidationError):
            self.about_info.delete()


class AboutSkillTestCase(TestCase):
    def setUp(self):
        self.about = AboutInfo.objects.create(
            first_name="John",
            last_name="Doe",
            description="A test description."
        )

    def test_about_skill_creation(self):
        about_skill = AboutSkill.objects.create(
            name="Programming",
            display_order=1
        )
        self.assertEqual(str(about_skill), "Programming")

    def test_about_skill_duplicate_name(self):
        with self.assertRaises(IntegrityError):
            AboutSkill.objects.create(
                name="Programming",
                display_order=1
            )
            AboutSkill.objects.create(
                name="Programming",  # Utilisez le même nom pour provoquer une IntegrityError
                display_order=2
            )

    def test_about_skill_default_display_order(self):
        about_skill = AboutSkill.objects.create(
            name="Python"
        )
        self.assertEqual(about_skill.display_order, 1)

    def test_about_skill_auto_increment_display_order(self):
        AboutSkill.objects.create(
            name="JavaScript",
            display_order=1
        )
        about_skill = AboutSkill.objects.create(
            name="React"
        )
        self.assertEqual(about_skill.display_order, 2)

    def test_about_skill_about_info_relation(self):
        about_skill = AboutSkill.objects.create(
            name="Python",
            display_order=1
        )
        self.assertEqual(about_skill.about, self.about)

class SocialLinkTestCase(TestCase):
    def setUp(self):
        self.about = AboutInfo.objects.create(
            first_name="John",
            last_name="Doe",
            description="A test description."
        )

    def test_social_link_creation(self):
        social_link = SocialLink.objects.create(
            name="LinkedIn",
            url="https://www.linkedin.com/",
            icon_classes="fa fa-linkedin",
            display_order=1
        )
        self.assertEqual(str(social_link), "LinkedIn")

    def test_social_link_duplicate_name(self):
        with self.assertRaises(IntegrityError):
            SocialLink.objects.create(
                name="LinkedIn",
                url="https://www.linkedin.com/",
                icon_classes="fa fa-linkedin",
                display_order=1
            )
            SocialLink.objects.create(
                name="LinkedIn",  # Utilisez le même nom pour provoquer une IntegrityError
                url="https://www.linkedin.com/",
                icon_classes="fa fa-linkedin",
                display_order=2
            )

    def test_social_link_default_display_order(self):
        social_link = SocialLink.objects.create(
            name="Twitter",
            url="https://twitter.com/",
            icon_classes="fa fa-twitter"
        )
        self.assertEqual(social_link.display_order, 1)

    def test_social_link_auto_increment_display_order(self):
        SocialLink.objects.create(
            name="Facebook",
            url="https://www.facebook.com/",
            icon_classes="fa fa-facebook",
            display_order=1
        )
        social_link = SocialLink.objects.create(
            name="Instagram",
            url="https://www.instagram.com/",
            icon_classes="fa fa-instagram"
        )
        self.assertEqual(social_link.display_order, 2)

    def test_social_link_about_info_relation(self):
        social_link = SocialLink.objects.create(
            name="LinkedIn",
            url="https://www.linkedin.com/",
            icon_classes="fa fa-linkedin",
            display_order=1
        )
        self.assertEqual(social_link.about, self.about)
