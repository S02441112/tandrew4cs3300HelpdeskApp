from django.urls import path, include
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('tickets/', views.ticket_list_view, name='tickets'),
    path('tickets/<int:ticket_id>', views.ticket_detail_view, name='ticket-detail'),
    path('ticket/create_ticket/', views.create_ticket, name='ticket-create'),
    path('tickets/<int:ticket_id>/update/', views.update_ticket, name='ticket-update'),
    path('tickets/<int:ticket_id>/delete/', views.delete_ticket, name='ticket-delete'),
    
    # user accounts
    path('accounts/', include('django.contrib.auth.urls')),
    # the include('django.contrib.auth.urls') automatically maps all urls for login, logout, password_change, ... etc.
    path('accounts/register/', views.register_page, name='register-page'),
    path('user/', views.user_page, name = 'user_page'),

]
