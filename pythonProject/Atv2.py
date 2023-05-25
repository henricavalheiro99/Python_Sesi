while True:
    inicio = int(input("Bem-vindo ao site de cálculo da hipotenusa (digite 1 para continuar): "))
    if inicio == 1:
        break
c1 = float(input("Digite o valor do primeiro cateto: "))
c2 = float(input("Digite o valor do segundo cateto: "))
hipotenusa = ((c1*c1)+(c2*c2)) ** 0.5
print(f"O valor da hipotenusa é: {hipotenusa:.2f}")