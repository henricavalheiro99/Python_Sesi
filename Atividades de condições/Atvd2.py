while True:
    inicio = int(input("Bem-vindo ao programa que compara números (digite 1 para continuar): "))
    if inicio == 1:
        break
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um segundo número: "))
if num1 < num2:
    print(f"{num2} é maior que {num1}")
elif num1 == num2:
    print(f"{num1} é igual a {num2}")
else:
    print(f"{num1} é maior que {num2}")