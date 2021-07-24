from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clientes.views import ClientesViewSet

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
