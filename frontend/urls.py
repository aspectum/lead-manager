from django.urls import path

from . import views

urlpatterns = [
    path('leads', views.leads, name='leads'),
    path('leads/new', views.new_lead, name='new_lead'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]