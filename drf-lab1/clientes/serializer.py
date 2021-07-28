from clientes.helpers.clientevalidate import cpf_valido, nome_valido, rg_valido
from django.db.models import fields
from rest_framework import serializers
from clientes.models import Cliente
from clientes.helpers.clientevalidate import *


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer model clientes
    """
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': "CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {
                    'nome':  "O nome deve conter apenas letras"
                }
            )
        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': 'O campo RG deve conter 9 dígitos'}
            )
        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular': 'O campo celular deve seguir o padrão 11 91234-1234'}
            )
        return data
