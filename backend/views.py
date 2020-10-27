# from django.shortcuts import render
# from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import StatusLead, Lead, Customer, Opportunity
from backend.serializers import LeadSerializer, UserSerializer#, CustomerSerializer, OpportunitySerializer #,StatusLeadSerializer
from dataclasses import dataclass

UserModel = get_user_model()

@dataclass
class LeadDTO:
    id: int
    name: str
    phone: str
    email: str
    status: int

def _build_dto(data):
    return LeadDTO(
        id = data.get("id"),
        name = data.get("customer_name"),
        phone = data.get("customer_phone"),
        email = data.get("customer_email"),
        status = data.get("status_id")
    )

def _prepare_response(payload=None, action=None, result=None, errors=None):
    return  {
        "action": action,
        "result": result,
        "payload": payload,
        "errors": errors
    }

class LeadsDetail(APIView):
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return self.request.user.leads.get(pk=pk)


    def get(self, request, pk, format=None):
        try:
            lead = self.get_object(pk)
        except:
            res = _prepare_response(None, 'get', 'failure', 'Lead not found')
            return Response(res, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(lead)
        dto = _build_dto(serializer.data)
        res = _prepare_response(dto.__dict__, 'get', 'success')
        return Response(res)

    def put(self, request, pk, format=None):
        try:
            lead = self.get_object(pk)
        except:
            res = _prepare_response(None, 'put', 'failure', 'Lead not found')
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        # request.data["owner"] = self.request.user.id
        serializer = self.serializer_class(lead, data=request.data)
        if serializer.is_valid():

            # creating other stuff
            if lead.status_id.id == 1 and serializer.validated_data.get('status_id').id == 2:
                print('de 1 pra 2')
                # Create customer entry
                customer = Customer(lead_id=lead)
                customer.save()
            if lead.status_id.id == 2 and serializer.validated_data.get('status_id').id == 3:
                print('de 2 pra 3')
                oppos = lead.opportunities
                for oppo in oppos:
                    old_desc = oppo.description
                    new_desc = old_des + ' ' + serializer.validated_data.get('meeting_date')
                    oppo.update(description=new_desc)
                    oppo.save()
            # end





            serializer.save()
            dto = _build_dto(serializer.data)
            res = _prepare_response(dto.__dict__, 'put', 'success')
            print(res)
            return Response(res)
        else:
            dto = _build_dto(serializer.data)
            res = _prepare_response(dto.__dict__, 'put', 'failure', errors=serializer.errors)
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            lead = self.get_object(pk)
        except:
            res = _prepare_response(None, 'delete', 'failure', 'Lead not found')
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def permission_denied(self, request):
    #     if not request.successful_authenticator:
    #         res = _prepare_response(None, 'authentication', 'failure', errors={"detail": "Invalid username/password"})
    #         return Response(res, status=status.HTTP_401_UNAUTHORIZED)
    #     res = _prepare_response(None, 'authentication', 'failure', errors={"detail": "Invalid username/password"})
    #     return Response(res, status=status.HTTP_403_FORBIDDEN)


class LeadsList(APIView):
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        leads = self.request.user.leads.all()
        dtos = []
        payload = []
        for lead in leads:
            serializer = self.serializer_class(lead)
            dtos.append(_build_dto(serializer.data))
            payload.append(dtos[-1].__dict__)
        res = _prepare_response(payload, 'get', 'success')
        return Response(res)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            lead = serializer.save(owner=self.request.user)

            # Creating opportunities
            if request.data.get("checkRPA"):
                oppo = Opportunity(description='RPA ', lead_id=lead)
                oppo.save()
            if request.data.get("checkPD"):
                oppo = Opportunity(description='Produto Digital ', lead_id=lead)
                oppo.save()
            if request.data.get("checkANA"):
                oppo = Opportunity(description='Analytics ', lead_id=lead)
                oppo.save()
            if request.data.get("checkBPM"):
                oppo = Opportunity(description='BPM ', lead_id=lead)
                oppo.save()
            # finished

            dto = _build_dto(serializer.data)
            res = _prepare_response(dto.__dict__, 'post', 'success')
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            dto = _build_dto(serializer.data)
            res = _prepare_response(dto.__dict__, 'post', 'failure', errors=serializer.errors)
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = _prepare_response(None, 'post', 'success')
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            res = _prepare_response(None, 'post', 'failure', errors=serializer.errors)
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

# class LeadsList(generics.ListCreateAPIView):
#     serializer_class = LeadSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return self.request.user.leads.all()

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class LeadsDetail(generics.RetrieveUpdateAPIView):
#     serializer_class = LeadSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return self.request.user.leads.all()

# class UserList(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]


















# API endpoints
# class StatusLeadViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = StatusLead.objects.all()
#     serializer_class = StatusLeadSerializer
#     permission_classes = [permissions.AllowAny]

# class LeadViewset(viewsets.ModelViewSet):
#     queryset = Lead.objects.all()
#     serializer_class = LeadSerializer
#     permission_classes = [permissions.AllowAny]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class CustomerViewset(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     permission_classes = [permissions.AllowAny]

# class OpportunityViewset(viewsets.ModelViewSet):
#     queryset = Opportunity.objects.all()
#     serializer_class = OpportunitySerializer
#     permission_classes = [permissions.AllowAny]

# # Need to fix permissions (Allow any for register(POST), but not for delete)
# class UserViewset(viewsets.ModelViewSet):
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]
