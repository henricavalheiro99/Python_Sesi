while True:
    inicio = int(input("Bem-vindo ao programa de prestações (digite 1 para continuar): "))
    if inicio == 1:
        break
valor = int(input("Digite o valor de sua última compra: "))
prestacoes = int(input("Digite o número de prestações: "))
cadaprestacao = valor / prestacoes
if cadaprestacao > 500:
    print(f"O valor de cada prestação é {cadaprestacao}, não é possível pagar")
else:
    print(f"O valor de cada prestação é {cadaprestacao}, paga aí meu cria")