from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from .models import Technology, Category, Project, ProjectCategory, ProjectTechnology
from common.models import FontAwesomeIcon


class TechnologyModelTest(TestCase):
    def setUp(self):
        self.icon = FontAwesomeIcon.objects.create(title='test_icon', css_classes='fa-test')
        self.technology = Technology.objects.create(name='Test Technology', icon=self.icon)

    def test_technology_name(self):
        expected_name = 'Test Technology'
        self.assertEqual(self.technology.name, expected_name)

    def test_technology_icon(self):
        expected_icon_name = 'test_icon'
        self.assertEqual(self.technology.icon.title, expected_icon_name)

    def test_technology_str(self):
        expected_str = 'Test Technology'
        self.assertEqual(str(self.technology), expected_str)

    def test_add_same_name_technology(self):
        with self.assertRaises(IntegrityError):
            icon = FontAwesomeIcon.objects.create(title='test_icon_2', css_classes='fa-test-2')
            technology = Technology.objects.create(name='Test Technology', icon=icon)
            technology.full_clean()


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_name(self):
        expected_name = 'Test Category'
        self.assertEqual(self.category.name, expected_name)

    def test_category_str(self):
        expected_str = 'Test Category'
        self.assertEqual(str(self.category), expected_str)

    def test_add_same_name_category(self):
        with self.assertRaises(IntegrityError):
            category = Category.objects.create(name='Test Category')
            category.full_clean()


class ProjectModelTest(TestCase):
    def setUp(self):
        self.icon = FontAwesomeIcon.objects.create(title='Test Icon', css_classes='test-class')
        self.technology = Technology.objects.create(name='Test Technology', icon=self.icon)
        self.category = Category.objects.create(name='Test Category')
        self.project = Project.objects.create(name='Test Project', description='Project Description')
        self.project_category = ProjectCategory.objects.create(project=self.project, category=self.category, display_order=1)
        self.project_technology = ProjectTechnology.objects.create(project_category=self.project_category, technology=self.technology, display_order=1)

    def test_project_creation(self):
        self.assertEqual(self.project.name, 'Test Project')
        self.assertEqual(self.project.description, 'Project Description')

    def test_project_category_creation(self):
        self.assertEqual(self.project_category.project.name, 'Test Project')
        self.assertEqual(self.project_category.category.name, 'Test Category')
        self.assertEqual(self.project_category.display_order, 1)

    def test_project_technology_creation(self):
        self.assertEqual(self.project_technology.project_category.project.name, 'Test Project')
        self.assertEqual(self.project_technology.project_category.category.name, 'Test Category')
        self.assertEqual(self.project_technology.technology.name, 'Test Technology')
        self.assertEqual(self.project_technology.display_order, 1)

