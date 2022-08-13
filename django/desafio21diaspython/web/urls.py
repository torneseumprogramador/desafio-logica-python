from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .controllers import contato_controller, home_controller, login_controller

urlpatterns = [
    path('', home_controller.index),
    path('sobre', home_controller.sobre),

    path('contato', contato_controller.index),
    path('contato/cadastrar', contato_controller.cadastrar),

    path('login', login_controller.index),
    path('logar', login_controller.logar),
    path('sair', login_controller.sair),

    path('html', views.html_bruto),
    path('json', views.json),
    path('xml', views.xml_bruto),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)










# urlpatterns = [
#     path('', home_controller.index),
#     path('sobre', home_controller.sobre),
#     path('contato', home_controller.contato),

#     path('html', views.html_bruto),
#     path('json', views.json),
#     path('xml', views.xml_bruto),
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
