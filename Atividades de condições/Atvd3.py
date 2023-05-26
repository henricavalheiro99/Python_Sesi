while True:
    inicio = int(input("Bem-vindo ao programa de números pares e ímpares (digite 1 para continuar): "))
    if inicio == 1:
        break
num = int(input("Digite um número: "))
if num %2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")