from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import gettext as _

from .models import AdminContact


class EmailSender:
    """
    Send emails to admin and user
    """
    def __init__(
        self,
        admin_notification_template='contact/emails/admin_message_notification.html',
        user_confirmation_template='contact/emails/user_message_confirmation.html',
        user_notification_template='contact/emails/user_message_notification.html',
    ):
        admin_contact = AdminContact.objects.first()
        self.admin_email = admin_contact.admin_email
        self.website_email = admin_contact.website_email
        self.admin_notification_template = admin_notification_template
        self.user_confirmation_template = user_confirmation_template
        self.user_notification_template = user_notification_template

    def send_notification_to_admin(self, message):
        thread = message.thread
        subject = _("New emails message") + f" - {thread.subject}"
        html_message = render_to_string(
            self.admin_notification_template,
            {'message': message})
        send_mail(
            subject=subject,
            message='',
            from_email=self.website_email,
            recipient_list=[self.admin_email],
            html_message=html_message,
        )

    def send_confirmation_to_user(self, message):
        thread = message.thread
        subject = _("Contact message received") + f" - {thread.subject}"
        html_message = render_to_string(
            self.user_confirmation_template,
            {'message': message}
        )
        send_mail(
            subject=subject,
            message='',
            from_email=thread.email,
            recipient_list=[thread.email],
            html_message=html_message,
        )

    def send_notification_to_user(self, message):
        thread = message.thread
        subject = _("We have replied to your message") + f" - {thread.subject}"
        html_message = render_to_string(
            self.user_notification_template,
            {'message': message}
        )
        send_mail(
            subject=subject,
            message='',
            from_email=self.website_email,
            recipient_list=[thread.email],
            html_message=html_message,
        )

