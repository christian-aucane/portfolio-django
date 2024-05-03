import uuid

from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import ContactThread, ContactMessage, AdminContact


class ContactThreadModelTests(TestCase):
    def test_save_unprocessed_thread(self):
        thread = ContactThread.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            subject="Test Subject"
        )

        self.assertFalse(thread.is_processed)
        self.assertIsNone(thread.processed_at)
        self.assertFalse(thread.is_archived)
        self.assertIsNone(thread.archived_at)

        thread.save()

        self.assertIsNone(thread.processed_at)
        self.assertIsNone(thread.archived_at)

    def test_save_processed_thread(self):
        thread = ContactThread.objects.create(
            name="Jane Doe",
            email="jane.doe@example.com",
            subject="Test Subject"
        )

        # Process the thread
        thread.is_processed = True
        thread.save()

        self.assertTrue(thread.is_processed)
        self.assertIsNotNone(thread.processed_at)

    def test_archive_unprocessed_thread(self):
        thread = ContactThread.objects.create(
            name="Unprocessed Thread",
            email="unprocessed@example.com",
            subject="Test Subject"
        )

        with self.assertRaises(ValueError):
            thread.is_archived = True
            thread.save()

    def test_archive_processed_thread(self):
        thread = ContactThread.objects.create(
            name="Processed Thread",
            email="processed@example.com",
            subject="Test Subject",
            is_processed=True
        )

        thread.is_archived = True
        thread.save()

        self.assertTrue(thread.is_archived)
        self.assertIsNotNone(thread.archived_at)


class ContactMessageModelTests(TestCase):
    def setUp(self):
        self.thread = ContactThread.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            subject="Test Subject"
        )

    def test_save_unchanged_message(self):
        message = ContactMessage.objects.create(
            thread=self.thread,
            sender="user",
            message="Test Message"
        )

        self.assertIsNone(message.save())

    def test_new_contact_message_with_gdpr_consent(self):
        message = ContactMessage.new_contact(
            name="Jane Doe",
            email="jane.doe@example.com",
            subject="New Contact Subject",
            message="New Contact Message",
            gdpr_consent=True
        )
        thread = message.thread
        self.assertEqual(thread.name, "Jane Doe")
        self.assertEqual(thread.email, "jane.doe@example.com")
        self.assertEqual(thread.subject, "New Contact Subject")
        self.assertTrue(thread.gdpr_consent)

        self.assertEqual(message.message, "New Contact Message")

        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactThread.objects.count(), 2)

        message = ContactMessage.objects.last()
        thread = ContactThread.objects.get(subject="New Contact Subject")

        self.assertEqual(message.thread, thread)
        self.assertEqual(message.sender, "user")
        self.assertEqual(message.message, "New Contact Message")

    def test_new_contact_message_without_gdpr_consent_fail(self):
        message = ContactMessage.new_contact(
            name="Jane Doe",
            email="jane.doe@example.com",
            subject="New Contact Subject",
            message="New Contact Message",
        )
        self.assertEqual(message, None)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertEqual(ContactThread.objects.count(), 1)

    def test_add_message_to_thread(self):
        ContactMessage.add_message_to_thread(
            thread_uuid=self.thread.uuid,
            email="john.doe@example.com",
            message="Reply Message"
        )

        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactThread.objects.count(), 1)

        message = ContactMessage.objects.first()
        thread = ContactThread.objects.first()

        self.assertEqual(message.thread, thread)
        self.assertEqual(message.sender, "user")
        self.assertEqual(message.message, "Reply Message")

    def test_add_message_to_nonexistent_thread(self):
        result = ContactMessage.add_message_to_thread(
            thread_uuid=uuid.uuid4(),
            email="nonexistent@example.com",
            message="Nonexistent Message"
        )

        self.assertFalse(result)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertEqual(ContactThread.objects.count(), 1)

    def test_add_message_to_invalid_uuid(self):
        result = ContactMessage.add_message_to_thread(
            thread_uuid="invalid_uuid",
            email="invalid@example.com",
            message="Invalid Message"
        )

        self.assertFalse(result)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertEqual(ContactThread.objects.count(), 1)


class AdminContactTests(TestCase):

    def test_unique_admin_contact_creation(self):
        with self.assertRaises(ValidationError):
            AdminContact.objects.create(
                admin_email='another_admin@example.com',
                website_email='another_website@example.com'
            )

    def test_access_admin_contact(self):
        admin_contact = AdminContact.objects.first()
        self.assertIsNotNone(admin_contact)
        self.assertEqual(admin_contact.admin_email, 'admin@example.com')
        self.assertEqual(admin_contact.website_email, 'website@example.com')

    def test_modify_admin_contact(self):
        admin_contact = AdminContact.objects.first()
        admin_contact.admin_email = 'another_admin@example.com'
        admin_contact.website_email = 'another_website@example.com'
        admin_contact.save()
        self.assertEqual(admin_contact.admin_email, 'another_admin@example.com')
        self.assertEqual(admin_contact.website_email, 'another_website@example.com')
