# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import TicketForm, CreateUserForm, UserForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin # only for class based views
from django.contrib import messages
from .decorators import allowed_users

# Create views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
# Render index.html
    ##########################################################
    ##########################################################
    all_tickets = Ticket.objects.all()
    return render( request, 'helpdesk_app/index.html', {'all_tickets':all_tickets})

@login_required
@allowed_users(allowed_roles = ['Help-Desk'])
def create_ticket(request):
    form = TicketForm()

    if request.method == 'POST':
        project_data = request.POST.copy()
        form = TicketForm(request.POST)
        
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket-detail', ticket_id=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'helpdesk_app/ticket_form.html', {'form': form})

@login_required
@allowed_users(allowed_roles = ['Help-Desk'])
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

@login_required
@allowed_users(allowed_roles = ['Help-Desk'])
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        if 'submit' in request.POST:
            ticket.delete()
            return redirect('index')
        elif 'cancel' in request.POST:
            return redirect('ticket-detail', ticket_id)
        return redirect('index')
    return render(request, 'helpdesk_app/delete_confirmation_form.html', {'ticket': ticket})


def TicketDetailView(request, ticket_id):
    ticket =Ticket.objects.get(pk=ticket_id)

    # check if user is Help-Desk (ticket delete and edit)
    is_help_desk = request.user.groups.filter(name='Help-Desk').exists()

    context = { 'ticket': ticket, 'is_help_desk': is_help_desk,}
    
    return render(request, 'helpdesk_app/ticket_detail.html', context)

@login_required
@allowed_users(allowed_roles = ['Help-Desk'])
def TicketListView(request):
    # check if user is Help-Desk (ticket creation)
    is_help_desk = request.user.groups.filter(name='Help-Desk').exists()

    all_tickets = Ticket.objects.all()

    #context = { 'is_help_desk': is_help_desk,}
    return render( request, 'helpdesk_app/ticket_list.html', {'all_tickets':all_tickets})

def registerPage(request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Viewer-Only')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('user_page')
        
        context = {'form':form}
        return render(request, 'registration/register.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['Viewer-Only', 'Help-Desk'])
def userPage(request):
    user = request.user
    form =  UserForm(instance = user)

    # Reset initial data to empty strings
    form.initial['username'] = ''
    form.initial['email'] = ''

    if request.method == 'POST':
        form = UserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('user_page')

    context = {'form': form, 'user': user,}
    return render(request, 'helpdesk_app/user.html', context)



