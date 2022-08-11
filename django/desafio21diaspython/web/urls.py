from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('sobre', views.sobre),
    path('contato', views.contato),

    path('html', views.html_bruto),
    path('json', views.json),
    path('xml', views.xml_bruto),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
