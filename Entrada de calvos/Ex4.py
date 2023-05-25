while True:
    inicio = int(input("Bem-vindo ao site de cálculo da área e do perímetro (digite 1 para continuar): "))
    if inicio == 1:
        break
altura = int(input("Digite o valor da altura: "))
base = int(input("Sigite o valor da base: "))
area = altura * base
perimetro = (2*altura) + (2*base)
print(f"O valor da perímetro e do área são, respectivamente, {perimetro} e {area}")