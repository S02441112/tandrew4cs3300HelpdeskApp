# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
# Render index.html
    return render( request, 'helpdesk_app/index.html')
