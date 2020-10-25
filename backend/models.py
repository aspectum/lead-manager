from django.db import models
from django.conf import settings

# Create your models here.
class StatusLead(models.Model):
    description = models.CharField(max_length=100)

class Lead(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20, blank=True)
    customer_email = models.EmailField()
    status_id = models.ForeignKey(StatusLead, related_name='leads', on_delete=models.CASCADE) # Cascade?
    # next line is so that a user can only access their own leads
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='leads', on_delete=models.CASCADE) # Cascade?

class Customer(models.Model):
    lead_id = models.OneToOneField(Lead, on_delete=models.CASCADE)

class Opportunity(models.Model):
    OPPORTUNITY_CHOICES = [
        ('RPA', 'RPA'),
        ('PD', 'Produto Digital'),
        ('ANA', 'Analytics'),
        ('BPM', 'BPM'),
    ]

    lead_id = models.ForeignKey(Lead, related_name='opportunies', on_delete=models.CASCADE)
    description = models.CharField(max_length=3, choices=OPPORTUNITY_CHOICES)