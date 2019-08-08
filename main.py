

from GSC import GSC


print("Validador de CEP de Gotham City")

validador = GSC


while True:
    CEP = input("\ninsisra o CEP a ser verificado - 0 para sair: ")
    if CEP == "0" : break
    try:
        resultado = validador.validar_cep(CEP)
        if resultado == True:
            print("O Cep é Válido")
        else:
            print("O Cep digitado não é válido")
    except ValueError:
        print("Não foi possível validar o CPF - Formatação inválida")
        continue
