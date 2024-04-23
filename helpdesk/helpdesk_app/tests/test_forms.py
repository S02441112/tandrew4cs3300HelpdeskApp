from django.test import TestCase
from helpdesk_app.forms import TicketForm, CreateUserForm, UserForm
from helpdesk_app.models import Ticket
from django.contrib.auth.models import User


class TicketFormTestCase(TestCase):
    def testTicketFormValid(self):
        form_data = {
            'requester_name': 'John Doe',
            'subject': 'Test Ticket',
            'description': 'This is a test ticket.',
            'assignee': 'Bob',
            'priority': '3',
            'contact_email': 'john.doe@example.com'
        }
        form = TicketForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        # If the form is valid save it
        if form.is_valid():
            ticket = form.save()
            self.assertIsInstance(ticket, Ticket)
    
    def testTicketFormInvalid(self):
        # Test with missing required fields
        form_data = {
            'requester_name': '',
            'subject': '',
            'description': '',
            'assignee': '',
            'priority': '',
            'contact_email': ''
        }
        form = TicketForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('requester_name', form.errors)
        self.assertIn('subject', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('assignee', form.errors)
        self.assertIn('priority', form.errors)
        self.assertIn('contact_email', form.errors)

class CreateUserFormTest(TestCase):
    def test_valid_data(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_required_fields(self):
        form_data = {
            'username': '',  # Missing username
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_invalid_data(self):
        form_data = {
            'username': 'testuser',
            'email': 'notanemail',  # Invalid email
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_mismatched_passwords(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'wrongpassword'  # Mismatched passwords
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

class UserFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )

    def test_valid_data(self):
        form_data = {
            'username': 'newtestuser',
            'email': 'newemail@example.com'
        }
        form = UserForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(User.objects.get(pk=self.user.pk).username, 'newtestuser')
        self.assertEqual(User.objects.get(pk=self.user.pk).email, 'newemail@example.com')

    def test_missing_required_fields(self):
        form_data = {
            'username': '',  # Missing username
            'email': 'testuser@example.com'
        }
        form = UserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_invalid_data(self):
        form_data = {
            'username': 'testuser',  # Username already exists
            'email': 'invalidemail'  # Invalid email format
        }
        form = UserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_edge_cases(self):
        # Test with empty strings
        form_data = {
            'username': '',
            'email': ''
        }
        form = UserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

        # Test with very long input values
        long_string = 'a' * 256  # Exceeds typical length limits
        form_data = {
            'username': long_string,
            'email': f'{long_string}@example.com'
        }
        form = UserForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
