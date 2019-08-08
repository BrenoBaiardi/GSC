# O sistema dos correios de Gotham City tiveram um problema e perderam seu validador de CEPs. Hoje, sua missão é criar um validador de CEPs baseados em algumas pequenas regras listadas abaixo:
#
# 1. O CEP é um número maior que 100.000 e menor que 999999
# 2. O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares
#
#
# 121426 # Aqui, 1 é um dígito repetitivo alternado em par.
# 523563 # Aqui nenhum digito é alternado.
# 552523 # Aqui os números 2 e 5 são dígitos alternados repetitivos em par.
# 112233 # Aqui nenhum dígito é repetitivo alternado em par.

from unittest import TestCase
from GSC import GSC

class TestGSC(TestCase):

    def test_verificar_cep_dentro_de_range_aceito(self):
        CEP = str(112233)
        self.assertEqual(True, GSC.validar_cep(CEP))

    def test_verificar_cep_abaixo_de_range_aceito(self):
        CEP = "002233"
        with self.assertRaises(ValueError):
            GSC.validar_cep(CEP)

    def test_verificar_cep_acima_de_range_aceito(self):
        CEP = str(1999999)
        with self.assertRaises(ValueError):
            GSC.validar_cep(CEP)

    def test_verificar_cep_nao_repetido_alternado(self):
        CEP = str(112233)
        self.assertEqual(True, GSC.validar_cep(CEP))

    def test_verificar_cep_nao_alternado(self):
        CEP = str(523563)
        self.assertEqual(True, GSC.validar_cep(CEP))

    def test_verificar_todos_numeros_repetidos(self):
        CEP = str(999999)
        self.assertEqual(False, GSC.validar_cep(CEP))

    def test_verificar_1_digito_repetido_alternado_par_no_comeco(self):
        CEP = str(121426)
        self.assertEqual(False, GSC.validar_cep(CEP))

    def test_verificar_1_digito_repetido_alternado_par_no_meio(self):
        CEP = str(123256)
        self.assertEqual(False, GSC.validar_cep(CEP))

    def test_verificar_1_digito_repetido_alternado_par_no_fim(self):
        CEP = str(163252)
        self.assertEqual(False, GSC.validar_cep(CEP))

    def test_verificar_2_digitos_repetidos_alternados_pares(self):
        CEP = str(552523)
        self.assertEqual(False, GSC.validar_cep(CEP))

    def test_verificar_entrada_de_CEP_por_texto(self):
        CEP = str(112233)
        self.assertEqual(True, GSC.validar_cep(CEP))

    def test_verificar_entrada_de_CEP_por_numero(self):
        CEP = 112233
        self.assertEqual(True, GSC.validar_cep(CEP))

    def test_verificar_entrada_de_CEP_texto_formatado(self):
        try:
            CEP = '1-1-2-2-3-3'
            GSC.validar_cep(CEP)
            CEP = '1.1.2.2.3.3'
            GSC.validar_cep(CEP)
            CEP = '1 1 2 2 3 3'
            GSC.validar_cep(CEP)
            CEP = '11 22 33'
            GSC.validar_cep(CEP)
        except:
            self.fail()
