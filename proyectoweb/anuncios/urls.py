from django.urls import path
from . import views
from django.conf import settings

from django.urls import path


urlpatterns = [
    path('home/', views.home, name='home'),
    #path('', views.hora_actual, name='hora_actual'),
    path('', views.anuncio_list, name='anuncios_list'),
    path('anuncios/profiles', views.precio, name='precio'),
    path('anuncios/contacto', views.contacto, name='contacto'),
 path('anuncios/diseño', views.contacto, name='diseño'),





     




    # ... more URL patterns here

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
    document_root = settings.MEDIA_ROOT)