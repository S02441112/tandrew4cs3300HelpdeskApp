from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Ticket

@receiver(post_save, sender=Ticket)
def ticket_done_email_notification(sender, instance, created, **kwargs):
    # Check if the ticket's is_done field changed from False to True
    if not created and instance.is_done:
        # Render email content from a template
        email_content = render_to_string('helpdesk_app/ticket_done_email.html', {'ticket': instance})
        
        # Send email
        send_mail(
            subject='Your Ticket is Complete',
            message=email_content,
            from_email='tylerma2102@gmail.com',  # Use same email address in settings
            recipient_list=[instance.contact_email],
            fail_silently=False,
            html_message=email_content,  # Use the HTML message
        )
