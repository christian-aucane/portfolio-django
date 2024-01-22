from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Skill, FontAwesomeIcon

class SkillModelTests(TestCase):
    def setUp(self):
        self.icon = FontAwesomeIcon.objects.create(
            title="Python",
            classes="fab fa-python"
        )

    def test_skill_creation(self):
        skill = Skill.objects.create(
            name="Django",
            category="framework",
            icon=self.icon
        )
        self.assertEqual(str(skill), "Django")
        self.assertEqual(skill.category, "framework")
        self.assertEqual(skill.icon, self.icon)

    def test_skill_duplicate_name_and_category(self):
        with self.assertRaises(IntegrityError):
            Skill.objects.create(
                name="Django",
                category="framework",
                icon=self.icon
            )
            Skill.objects.create(
                name="Django",
                category="framework",
                icon=self.icon
            )

    def test_skill_without_icon(self):
        with self.assertRaises(IntegrityError):
            Skill.objects.create(
                name="Django",
                category="framework"
            )

    def test_skill_with_invalid_category(self):
        with self.assertRaises(ValidationError):
            skill = Skill.objects.create(name="Django", category="invalid_category", icon=self.icon)
            skill.full_clean()