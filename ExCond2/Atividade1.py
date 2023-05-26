while True:
    inicio = int(input("Bem-vindo ao programa de resultados de jogos (digite 1 para continuar): "))
    if inicio == 1:
        break
time1 = str(input("Digite o nome do primeiro time: "))
time2 = str(input("Digite o nome do segundo time: "))
num1 = int(input("Digite o número de gols do primeiro time: "))
num2 = int(input("Digite o número de gols do segundo time: "))
if num1 < num2:
    print(f"{time2} venceu o {time1} com placar de {num2} x {num1}")
elif num1 == num2:
    print(f"{time1} empatou com {time2} com placar de {num1} x {num2}")
else:
    print(f"{time1} venceu o {time2} com placar de {num1} x {num2}")