# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.views import generic

# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
# Render index.html
    ##########################################################
    ##########################################################
    all_tickets = Ticket.objects.all()
    print("All tickets", all_tickets)
    return render( request, 'helpdesk_app/index.html', {'all_tickets':all_tickets})

class TicketListView(generic.ListView):
   model = Ticket
class TicketDetailView(generic.DetailView):
    model = Ticket