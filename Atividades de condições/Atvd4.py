while True:
    inicio = int(input("Bem-vindo ao programa de cálculo da maioridade (digite 1 para continuar): "))
    if inicio == 1:
        break
nome = str(input("Digite seu nome: "))
nascimento = int(input("Digite o ano de seu nascimento: "))
idade = 2023 - nascimento
if idade >= 18:
    print(f"{nome} possui {idade} anos, logo é maior de idade")
else:
    print(f"{nome} possui {idade} anos, logo é menor de idade")