from django.forms import ModelForm
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('requester_name', 'is_done', 'contact_email', 'subject', 'description', 'assignee', 'priority')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']