from django.urls import path
from . import views
from django.conf import settings



urlpatterns = [
    #path('', views.hora_actual, name='hora_actual'),
    path('orlas', views.orla, name='orla_list')
    
    
    ]