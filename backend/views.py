from django.shortcuts import render
from rest_framework import viewsets, permissions
from backend.models import StatusLead, Lead, Customer, Opportunity
from backend.serializers import StatusLeadSerializer, LeadSerializer, CustomerSerializer, OpportunitySerializer

# API endpoints
class StatusLeadViewset(viewsets.ModelViewSet):
    queryset = StatusLead.objects.all()
    serializer_class = StatusLeadSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeadViewset(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class OpportunityViewset(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.IsAuthenticated]

