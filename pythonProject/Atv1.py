while True:
    inicio = int(input("Bem-vindo ao site de cálculo de média (digite 1 para continuar): "))
    if inicio == 1:
        break
nome = str(input("Digite o nome do aluno: "))
p1 = float(input("Digite o valor da primeira prova: "))
p2 = float(input("Digite o valor da segunda prova: "))
p3 = float(input("Digite o valor da terceira prova: "))
soma = p1 + p2 + p3
media = soma / 3
print(f"O valor da média do aluno {nome} é: {media:.2f}")