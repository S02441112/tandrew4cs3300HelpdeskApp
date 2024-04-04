# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import TicketForm

# Create views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
# Render index.html
    ##########################################################
    ##########################################################
    all_tickets = Ticket.objects.all()
    return render( request, 'helpdesk_app/index.html', {'all_tickets':all_tickets})

def create_ticket(request):
    form = TicketForm()

    if request.method == 'POST':
        project_data = request.POST.copy()
        #project_data['ticket_id'] = ticket_id
        form = TicketForm(request.POST)
        
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket-detail', pk=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'helpdesk_app/ticket_form.html', {'form': form})

def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket-detail', ticket_id)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'helpdesk_app/ticket_form.html', {'form': form})

def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        if 'submit' in request.POST:
            ticket.delete()
            return redirect('index')
        elif 'cancel' in request.POST:
            return redirect('ticket-detail', pk=ticket_id)
        return redirect('index')
    return render(request, 'helpdesk_app/delete_confirmation_form.html', {'ticket': ticket})

'''class TicketListView(generic.ListView):
   model = Ticket'''
class TicketDetailView(generic.DetailView):
    model = Ticket

def TicketListView(request):

    all_tickets = Ticket.objects.all()
    return render( request, 'helpdesk_app/ticket_list.html', {'all_tickets':all_tickets})