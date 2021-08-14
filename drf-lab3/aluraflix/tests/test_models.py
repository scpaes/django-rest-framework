from django.test import TestCase
from aluraflix.models import Programa


class ProgramaTestCas(TestCase):

    def setUp(self) -> None:
        self.programa = Programa(
            titulo = 'Programa Test',
            data_lancamento = '2003-07-07'
        )

    
    def test_valores_default(self):
        self.assertEquals(self.programa.titulo, 'Programa Test')
        self.assertEquals(self.programa.tipo, 'F')
        self.assertEquals(self.programa.data_lancamento, '2003-07-07')
        self.assertEquals(self.programa.likes, 0)
        self.assertEquals(self.programa.dislikes, 0)