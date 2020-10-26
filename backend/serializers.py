from django.contrib.auth import get_user_model
from rest_framework import serializers
from backend.models import StatusLead, Lead, Customer, Opportunity

UserModel = get_user_model()

# class StatusLeadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StatusLead
#         fields = ('__all__') 

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('__all__') 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__') 

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ('__all__') 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    leads = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'leads') 
