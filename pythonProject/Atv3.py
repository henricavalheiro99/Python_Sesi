while True:
    inicio = int(input("Bem-vindo ao site de cálculo de salário (digite 1 para continuar): "))
    if inicio == 1:
        break
nome = str(input("Digite seu nome: "))
salario = float(input("Digite o seu salário: "))
aumento = float(input("Digite um percentual de aumento: "))
percentual = (salario/100) * aumento
salarionovo = salario + percentual
print(f"O salário novo de {nome} é: {salarionovo:.2f}")