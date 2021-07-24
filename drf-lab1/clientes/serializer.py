from django.db.models import fields
from rest_framework import serializers
from clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    """Serializer model clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'