from django.shortcuts import render, redirect
from rest_framework.reverse import reverse
from django.contrib import auth
import requests

# Create your views here.
def leads(request):

    leads = requests.get(request.build_absolute_uri(reverse('api:leads')), 
                            auth=(request.session.get('CredentialsUser'), request.session.get('CredentialsPass'))).json()

    context = {
        'leads': leads['payload']
    }

    print(leads['payload'])

    return render(request, 'leads.html', context)

def new_lead(request):
    return render(request, 'new_lead.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        # Getting form values
        username = request.POST['inputUsername']
        password = request.POST['inputPassword']

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
        username = request.POST['inputUsername']
        password = request.POST['inputPassword']
        password2 = request.POST['inputPasswordConfirmation']

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
