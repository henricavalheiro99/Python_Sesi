while True:
    inicio = int(input("Bem-vindo ao programa de cálculo de média (digite 1 para continuar): "))
    if inicio == 1:
        break
nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
if media < 6:
    print(f"O aluno {nome} está reprovado com média {media:.2f}")
else:
    print(f"O aluno {nome} está aprovado com média {media:.2f}")