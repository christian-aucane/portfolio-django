import uuid as uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ContactThread(models.Model):
    class Meta:
        verbose_name = _("Contact Thread")
        verbose_name_plural = _("Contact Threads")
        ordering = ["-created_at"]

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False,
                            verbose_name=_("UUID"))
    name = models.CharField(max_length=255,
                            verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email address"))
    subject = models.CharField(max_length=255,
                               verbose_name=_("Subject"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    is_processed = models.BooleanField(default=False, verbose_name=_("Processed"))
    processed_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Processed at"))
    is_archived = models.BooleanField(default=False, verbose_name=_("Archived"))
    archived_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Archived at"))

    def __str__(self):
        return f"{self.name} - {self.subject}"

    def save(self, *args, **kwargs):
        if self.pk:
            original_instance = ContactThread.objects.get(pk=self.pk)
            is_processed_changed = original_instance.is_processed != self.is_processed
            if is_processed_changed:
                if self.is_processed:
                    self.processed_at = timezone.now()
                else:
                    self.processed_at = None
            is_archived_changed = original_instance.is_archived != self.is_archived
            if is_archived_changed:
                if self.is_archived:
                    if self.is_processed:
                        self.archived_at = timezone.now()
                    else:
                        raise ValueError("Can't archive an unprocessed thread")
                else:
                    self.archived_at = None

        return super().save(*args, **kwargs)


class ContactMessage(models.Model):
    class Meta:
        verbose_name = _("Contact Message")
        verbose_name_plural = _("Contact Messages")
        ordering = ["created_at"]

    SENDER_CHOICES = [
        ("admin", _("Admin")),
        ("user", _("User")),
    ]

    thread = models.ForeignKey(ContactThread, on_delete=models.CASCADE,
                               related_name="messages",
                               verbose_name=_("Thread"))
    sender = models.CharField(max_length=255, choices=SENDER_CHOICES,
                              verbose_name=_("Sender"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_("Created at"))

    def __str__(self):
        return f"{self.thread} - {self.created_at}"

    def save(self, *args, **kwargs):
        if self.pk:
            original_instance = ContactMessage.objects.get(pk=self.pk)
            if original_instance.has_changed():
                return self
        return super().save(*args, **kwargs)

    @classmethod
    def new_contact(cls, name, email, subject, message):
        thread = ContactThread(name=name, email=email, subject=subject)
        thread.save()
        cls.objects.create(thread=thread, sender="user", message=message)
        return True

    @classmethod
    def add_message_to_thread(cls, thread_uuid, email, message):
        try:
            thread = ContactThread.objects.get(uuid=thread_uuid, email=email)
            cls.objects.create(thread=thread, sender="user", message=message)
        except ContactThread.DoesNotExist:
            return False
