from django.db import models
from django.urls import reverse
#import os 

# Create your models here.

class Ticket(models.Model):

    ASSIGNEE = (
        ('Bob', 'Bob'),
        ('Steve', 'Steve'),
        ('Sarah', 'Sarah'),
        ('Yui', 'Yui'),
    )
    PRIORITY = (
        ('1','Highest'),
        ('2','High'),
        ('3','Medium'),
        ('4','Low'),
        ('5','Lowest'),
    )
    requester_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200) # required
    is_done = models.BooleanField(default=False) # True when tecket is complete
    description = models.TextField(blank = False) # required
    assignee = models.CharField(max_length=200, choices=ASSIGNEE, blank = False) # blank = True makes field optional
    priority = models.CharField(max_length=1, choices=PRIORITY, blank = False) # blank = True makes field optional
    contact_email = models.CharField(max_length=200)

    # screenshot = models.ImageField(upload_to ='uploads/') 

    def __str__(self):
        return self.requester_name
    def get_absolute_url(self):
        return reverse("ticket-detail", args=[str(self.id)])