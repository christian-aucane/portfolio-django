from smtplib import SMTPException

from django.core.mail import send_mail
from django.db import transaction
from django.http import JsonResponse
from django.views import View

from contact.models import ContactMessage
from contact.utils import EmailSender


# Create your views here.
class ContactFormSubmissionView(View):

    # POST
    @transaction.atomic
    def post(self, request, *args, **kwargs):

        form_data = request.POST

        name = form_data.get("name")
        email = form_data.get("email")
        subject = form_data.get("subject")
        message = form_data.get("message")
        gdpr_consent = form_data.get("consent") == "on"

        message = ContactMessage.new_contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
            gdpr_consent=gdpr_consent
        )
        if message is not None:
            email_sender = EmailSender()
            try:
                email_sender.send_notification_to_admin(message)
                email_sender.send_confirmation_to_user(message)

                return JsonResponse({"status": "success"}, status=200)

            except SMTPException as e:
                print(f"SMTPException: {str(e)}")  # TODO : remplacer par un log
                transaction.rollback()
                return JsonResponse(
                    {
                        "status": "error",
                        "message": _("Failed to send notification or confirmation")
                    }, status=500
                )
        else:
            return JsonResponse(
                {"status": "error",
                 "message": "Failed to create emails message"
                 }, status=500
            )
