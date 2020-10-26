from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('leads', views.leads, name='leads'),
    path('leads/new', views.new_lead, name='new_lead'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]