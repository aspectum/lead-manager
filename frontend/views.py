from django.shortcuts import render

# Create your views here.
def leads(request):

    context = {
        'leads': [
  {
    "id": 1,
    "date": "2020-10-25T23:43:51.166766Z",
    "customer_name": "teste",
    "customer_phone": "123",
    "customer_email": "teste@teste.com",
    "status_id": 2,
    "owner": 4
  },
  {
    "id": 2,
    "date": "2020-10-25T23:44:05.778064Z",
    "customer_name": "teste2311323",
    "customer_phone": "123123124124",
    "customer_email": "teste22@teste.com",
    "status_id": 1,
    "owner": 4
  },
  {
    "id": 3,
    "date": "2020-10-25T23:44:14.367905Z",
    "customer_name": "teste2311323",
    "customer_phone": "123123124124",
    "customer_email": "teste22@teste.com",
    "status_id": 2,
    "owner": 4
  },
  {
    "id": 4,
    "date": "2020-10-25T23:50:15.882494Z",
    "customer_name": "fedor",
    "customer_phone": "9999",
    "customer_email": "fedor@fedor.com",
    "status_id": 3,
    "owner": 1
  }
]
    }

    return render(request, 'leads.html', context)

def new_lead(request):
    return render(request, 'new_lead.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')