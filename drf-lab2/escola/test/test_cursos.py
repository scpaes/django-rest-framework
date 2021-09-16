from django.http import response
from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')

        self.curso1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso de teste', nivel='B'
        )
        self.curso2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso de teste 2', nivel='I'
        )

    def test_request_get(self):
        """
            request.GET endpoint /cursos/
        """

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post(self):
        """
            request.POST endpoint /cursos/
        """

        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso test',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete(self):
        """
            request.DELETE endpoint /cursos/<int:id>/
        """
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code,
                          status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_put(self):
        """
            request.PUT endpoint /cursos/<int:id>/
        """
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso test ATUALIZADO',
            'nivel': 'I'
        }

        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
