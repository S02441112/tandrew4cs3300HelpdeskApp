from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Ticket
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

@receiver(post_save, sender=Ticket)
def ticket_done_email_notification(sender, instance, created, **kwargs):
    # not Created ensures instace was not just created - only for exising ticket
    # Check if the ticket's is_done field changed from False to True
    if not created and instance.is_done:
        # Render email content from a template
        email_content = render_to_string('helpdesk_app/ticket_done_email.html', 
                                         {'ticket': instance})
        # Get sender's email address from an environment variable
        from_email = env('EMAIL_HOST_USER')
        # Send email
        send_mail(
            subject='Your Ticket is Complete', # Subject of email
            message=email_content, # Body of email
            from_email=from_email,  # Use same email address in settings.py
            recipient_list=[instance.contact_email],
            fail_silently=False,
            html_message=email_content,  # Use HTML message
        )
