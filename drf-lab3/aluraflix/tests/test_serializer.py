from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.programa = Programa(
            titulo = 'Programa Serializer test',
            data_lancamento = '2003-07-08',
        )

        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializer(self):
        """
            Teste para verificar se os campos do serializer estão sendo serializados. 
        """

        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'data_lancamento', 'likes', 'tipo']))


    def test_valor_dos_campos(self):
        """
            Teste para verificar se o valor dos campos serializados é igual a model
        """

        data = self.serializer.data
        self.assertEqual(self.programa.titulo, data['titulo'])
        self.assertEqual(self.programa.tipo, data['tipo'])
        self.assertEqual(self.programa.data_lancamento, data['data_lancamento'])
        self.assertEqual(self.programa.likes, data['likes'])