from django.test import TestCase
#from authentication.models import User
from helpdesk_app.models import Ticket
#from django.contrib.auth.models import User

class TicketModelTestCase(TestCase):
    def testTicketCreation(self):
        ticket = Ticket.objects.create(
            requester_name="John Doe",
            subject="Test Ticket",
            description="This is a test ticket.",
            assignee="Bob",
            priority="3",
            contact_email="john.doe@example.com"
        )

        # Check if the ticket was created successfully
        self.assertEqual(ticket.requester_name, "John Doe")
        self.assertEqual(ticket.subject, "Test Ticket")
        self.assertEqual(ticket.assignee, "Bob")
        self.assertEqual(ticket.priority, "3")
        self.assertEqual(ticket.contact_email, "john.doe@example.com")

        # Check other model fields and methods
        self.assertFalse(ticket.is_done)
        self.assertEqual(str(ticket), "John Doe")
        self.assertIsNotNone(ticket.get_absolute_url())