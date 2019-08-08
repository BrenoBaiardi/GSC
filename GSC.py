import re

class GSC():

    @staticmethod
    def validar_cep(CEP):
        CEP = str(CEP)
        CEP = "".join(re.findall('\d+', CEP))
        if len(CEP) <= 6 and CEP[0] != '0':
            for numero in CEP:
                pattern = a = re.escape(numero) + r"[0-9]" + re.escape(numero)
                if re.search(pattern,CEP):
                    return False
            return True
        else:
            raise ValueError("CEP informado não possui Valor Válido para verificação")