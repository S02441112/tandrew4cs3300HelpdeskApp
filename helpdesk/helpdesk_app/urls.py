from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('tickets/', views.TicketListView.as_view(), name='tickets'),
    path('tickets/<int:pk>', views.TicketDetailView.as_view(), name='ticket-detail'),
]
