from django.contrib import admin
from django.urls import path,include
from tercera_entrega.views import *
from AppComercio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",inicio,name="inicio"),
    path("AppComercio/",include("AppComercio.urls")),    
]
