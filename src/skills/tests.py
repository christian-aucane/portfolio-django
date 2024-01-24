from collections import defaultdict

from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Skill, FontAwesomeIcon


class SkillModelTests(TestCase):
    def setUp(self):
        self.icon, _ = FontAwesomeIcon.objects.get_or_create(
            title="Python",
            css_classes="fab fa-python"
        )

        self.icon_python, _ = FontAwesomeIcon.objects.get_or_create(
            title="Python",
            css_classes="fab fa-python"
        )
        self.icon_js, _ = FontAwesomeIcon.objects.get_or_create(
            title="JavaScript",
            css_classes="fab fa-js"
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

    def test_get_skills_by_category(self):
        python_skill = Skill.objects.create(name="Django", category="framework", icon=self.icon_python)
        js_skill = Skill.objects.create(name="React", category="framework", icon=self.icon_js)
        python_tool = Skill.objects.create(name="Flask", category="language", icon=self.icon_python)

        skills_by_category = Skill.get_skills_by_category()

        expected_result = defaultdict(list)

        expected_result['framework'].extend([python_skill, js_skill])
        expected_result['language'].append(python_tool)
        expected_result['workflow'] = []

        self.assertEqual(skills_by_category, expected_result)
