from django.test import TestCase
from django.urls import reverse
from helpdesk_app.models import Ticket
from django.contrib.auth.models import User

class TicketDetailViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.ticket = Ticket.objects.create(
            requester_name='John Doe',
            subject='Test Ticket',
            description='This is a test ticket.',
            assignee='Bob',
            priority='3',
            contact_email='john.doe@example.com'
        )

    def test_ticket_detail_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('ticket-detail', args=[self.ticket.id]))
        self.assertEqual(response.status_code, 200) # success code
        
        # Check if the response contains the ticket details
        self.assertContains(response, 'John Doe')
        self.assertContains(response, 'Test Ticket')
