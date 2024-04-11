# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import TicketForm, CreateUserForm, UserForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import allowed_users

# Create views here.
@login_required
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
            return redirect('ticket-detail', pk=ticket.pk)
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
            return redirect('ticket-detail', pk=ticket_id)
        return redirect('index')
    return render(request, 'helpdesk_app/delete_confirmation_form.html', {'ticket': ticket})


class TicketDetailView(generic.DetailView):
    model = Ticket

@login_required
@allowed_users(allowed_roles = ['Help-Desk'])
def TicketListView(request):

    all_tickets = Ticket.objects.all()
    return render( request, 'helpdesk_app/ticket_list.html', {'all_tickets':all_tickets})

def registerPage(request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Viewer-Only')
            user.groups.add(group)
            #student = Student.objects.create(user=user)
            #portfolio = Portfolio.objects.create()
            #student.portfolio = portfolio
            #student.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
        context = {'form':form}
        return render(request, 'registration/register.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['Viewer-Only'])
def userPage(request):
    user = request.user
    form =  UserForm(instance = user)
    print('user', user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()

    context = {'user': user, 'form': form}
    return render(request, 'helpdesk_app/user.html')



