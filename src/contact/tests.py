import uuid
from django.test import TestCase
from django.utils import timezone
from .models import ContactThread, ContactMessage


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

        # Save the thread without processing
        thread.save()

        # Check that processed_at and archived_at remain unchanged
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

        # Attempt to archive an unprocessed thread should raise ValueError
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

        # Archive a processed thread
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

        # Saving an unchanged message should not create a new instance
        self.assertIsNone(message.save())

    def test_new_contact_message(self):
        # Create a new contact message
        ContactMessage.new_contact(
            name="Jane Doe",
            email="jane.doe@example.com",
            subject="New Contact Subject",
            message="New Contact Message"
        )

        # Check that the message and thread were created
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactThread.objects.count(), 2)

        message = ContactMessage.objects.last()
        thread = ContactThread.objects.get(subject="New Contact Subject")

        self.assertEqual(message.thread, thread)
        self.assertEqual(message.sender, "user")
        self.assertEqual(message.message, "New Contact Message")

    def test_add_message_to_thread(self):
        # Add a message to an existing thread
        ContactMessage.add_message_to_thread(
            thread_uuid=self.thread.uuid,
            email="john.doe@example.com",
            message="Reply Message"
        )

        # Check that the message was added to the existing thread
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactThread.objects.count(), 1)

        message = ContactMessage.objects.first()
        thread = ContactThread.objects.first()

        self.assertEqual(message.thread, thread)
        self.assertEqual(message.sender, "user")
        self.assertEqual(message.message, "Reply Message")

    def test_add_message_to_nonexistent_thread(self):
        # Attempting to add a message to a nonexistent thread should return False
        result = ContactMessage.add_message_to_thread(
            thread_uuid=uuid.uuid4(),
            email="nonexistent@example.com",
            message="Nonexistent Message"
        )

        self.assertFalse(result)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertEqual(ContactThread.objects.count(), 1)

    def test_add_message_to_invalid_uuid(self):
        # Attempting to add a message with an invalid UUID should return False
        result = ContactMessage.add_message_to_thread(
            thread_uuid="invalid_uuid",
            email="invalid@example.com",
            message="Invalid Message"
        )

        self.assertFalse(result)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertEqual(ContactThread.objects.count(), 1)