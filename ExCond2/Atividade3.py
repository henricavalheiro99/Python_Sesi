while True:
    inicio = int(input("Bem-vindo ao programa que classifica nadadores (digite 1 para continuar): "))
    if inicio == 1:
        break
nome = str(input("Digite seu nome: "))
idade = int(input("Digite a sua idade: "))
if idade < 5:
    print(f"{nome} não se enquadra, pois não possui idade")
elif idade >= 5 and idade <= 7:
    print(f"{nome} possui {idade} anos, ou seja, está no Infantil A")
elif idade >= 8 and idade <= 11:
    print(f"{nome} possui {idade} anos, ou seja, está no Infantil B")
elif idade >= 12 and idade <= 13:
    print(f"{nome} possui {idade} anos, ou seja, está no Juvenil A")
elif idade >=14 and idade <= 17:
    print(f"{nome} possui {idade} anos, ou seja, está no Juvenil B")
else:
    print(f"{nome} possui {idade} anos, ou seja, está no adultos")