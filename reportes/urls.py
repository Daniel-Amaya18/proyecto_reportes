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
from . import views

urlpatterns = [
    path('torneo/<int:id_t>', views.torneo, name="torneo_api"),
    path('test_id', views.test_id, name="test_id"),
    path('test_aux', views.test_aux, name="test_aux"),
    path('torneo_test_id/<int:id_t>', views.torneo_test_id, name="torneo_test_id"),
    path('test_fecha', views.test_fecha, name="test_fecha"),
    path('test_fecha_aux', views.test_fecha_aux, name="test_fecha_aux"),
    path('torneo_test_fecha/<str:fecha_inicial>/<str:fecha_final>/', views.torneo_test_fecha, name="torneo_test_fecha"),
    # path('torneo/busqueda_fecha', torneos_fechas_api_view, name="torneos_fechas_api_view"),
]