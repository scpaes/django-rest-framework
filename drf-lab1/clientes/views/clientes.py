from clientes.serializer import ClienteSerializer
from clientes.models.clientes import Cliente
from rest_framework import viewsets


class ClientesViewSet(viewsets.ModelViewSet):
    """Clientes viewset"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer