from django.shortcuts import render, redirect
from rest_framework.reverse import reverse
from django.contrib import auth
import requests
from frontend.forms import DateTimeForm

def find_lead(leads, id):
    for lead in leads:
        if lead.get("id") == id:
            return lead
    return None

# Create your views here.
def leads(request):

    res = requests.get(request.build_absolute_uri(reverse('api:leads')), 
                            auth=(request.session.get('CredentialsUser'), request.session.get('CredentialsPass'))).json()

    

    if request.method == 'POST':
        print(request.POST)
        if 'datetime_field' in request.POST:
            print(request.POST.get('datetime_field'))

        lead_id = request.POST.get('origin')
        if lead_id is not None:
            lead = find_lead(res['payload'], int(lead_id))

            #popup for scheduling meeting



            payload = {
                "customer_name": lead['name'],
                "customer_phone": lead['phone'],
                "customer_email": lead['email'],
                "owner": request.user.id,
                "status_id": lead['status'] + 1
                # meeting date
            }


            res = requests.put(request.build_absolute_uri(reverse('api:lead_detail', kwargs={'pk': lead_id})),
                                data=payload,
                                auth=(request.session.get('CredentialsUser'), request.session.get('CredentialsPass')))
            if res.status_code == requests.codes.ok:
                #message congrats
                return redirect('leads')
            else:
                # messages.error
                print(res.json())
                return redirect('leads')

    context = {
        'leads': res['payload'],
        'form': DateTimeForm()
    }

    return render(request, 'leads.html', context)

def new_lead(request):
    if request.method == 'POST':
        # Getting form values
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        customer_email = request.POST.get('customer_email')
        checkRPA = request.POST.get('checkRPA')
        checkPD = request.POST.get('checkPD')
        checkANA = request.POST.get('checkANA')
        checkBPM = request.POST.get('checkBPM')

        payload = {
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "customer_email": customer_email,
            "checkRPA": checkRPA,
            "checkPD": checkPD,
            "checkANA": checkANA,
            "checkBPM": checkBPM,
            "owner": request.user.id,
            "status_id": 1
        }

        res = requests.post(request.build_absolute_uri(reverse('api:leads')),
                            data=payload,
                            auth=(request.session.get('CredentialsUser'), request.session.get('CredentialsPass')))
        if res.status_code == requests.codes.created:
            #message congrats

            return redirect('leads')
        else:
            # messages.error
            print(res.json())
            return redirect('new_lead')
    else:
        return render(request, 'new_lead.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        # Getting form values
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')

        res = requests.get(request.build_absolute_uri(reverse('api:leads')), auth=(username, password))
        if res.status_code == requests.codes.ok:
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            
            # This doesn't look very safe
            request.session['CredentialsUser'] = username
            request.session['CredentialsPass'] = password

            return redirect('leads')
        else:
            # messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'Logged out')
        return redirect('index')
    return redirect('index')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        # Getting form values
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')
        password2 = request.POST.get('inputPasswordConfirmation')

        if password != password2:
            # do something
            pass

        # more validation, maybe validate in backend

        res = requests.post(request.build_absolute_uri(reverse('api:users')), data={"username":username,"password":password})

        if res.status_code == requests.codes.created:
            # message all good now login

            return redirect('login')
        else:
            # messages.error(request, 'errors')
            return redirect('register')
    else:
        return render(request, 'register.html')

def index(request):
    if request.user.is_authenticated:
        return redirect('leads')
    else:
        return redirect('login')



    # res = requests.get(request.build_absolute_uri(reverse('api:leads')), auth=(request.session.get('CredentialsUser'), request.session.get('CredentialsPass')))
