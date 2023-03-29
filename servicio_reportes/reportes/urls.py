"""modulo_reportes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from .api import torneo_api_view, torneo_esp_api_view, torneos_fechas_api_view
from . import views

urlpatterns = [
    path('', views.torneos, name = 'torneos'),  # Quitar después
    path('torneo/', torneo_api_view, name="torneo_api"),
    path('torneo/<int:id_t>', torneo_esp_api_view, name="torneo_esp_api"),
    path('torneo/busqueda_fecha', torneos_fechas_api_view, name="torneos_fechas_api_view"),
]







# urlpatterns = [
    
#     # path('admin/', admin.site.urls),
# ]