while True:
    inicio = int(input("Bem-vindo ao programa de operações matemáticas (digite 1 para continuar): "))
    if inicio == 1:
        break
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = str(input("Escolha a operação matemática(soma, subtração, multiplicação ou divisão): "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
if operacao == "soma" or operacao == "SOMA":
    print(f"{soma}")
elif operacao == "subtração" or operacao == "SUBTRAÇÃO":
    print(f"{subtracao}")
elif operacao == "multiplicação" or operacao == "MULTIPLICAÇÃO":
    print(f"{multiplicacao:.2f}")
elif operacao == "divisão" or operacao == "DIVISÃO":
    print(f"{divisao:.2f}")
