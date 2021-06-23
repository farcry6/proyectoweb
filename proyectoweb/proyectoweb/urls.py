"""proyectoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from pagina import views
from orla import views
from django.conf.urls import url


from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from anuncios import views         warning

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/', views.home, name='home'),
    #path('', views.hora_actual, name='hora_actual')
    path('',include('anuncios.urls')),

    path('',include('sendmail.urls')),
    path('orlas/', views.orla_list, name='orlas'),


 




    

]