from rest_framework import serializers
from backend.models import StatusLead, Lead, Customer, Opportunity

# Do I need to add user endpoint?

class StatusLeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusLead
        fields = ('__all__') 

class LeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusLead
        fields = ('__all__') 

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__') 

class OpportunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opportunity
        fields = ('__all__') 