while True:
    inicio = int(input("Bem-vindo ao site de cálculo de potências (digite 1 para continuar): "))
    if inicio == 1:
        break
num = int(input("Digite um número inteiro: "))
elevado = int(input("Digite a potência: "))
potencia = num**elevado
print(f"O valor da potência é: {potencia}")

