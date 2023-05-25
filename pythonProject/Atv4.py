while True:
    inicio = int(input("Bem-vindo ao site de cálculo de volume de cilíndros (digite 1 para continuar): "))
    if inicio == 1:
        break
pi = 3.141
raio = float(input("Digite o valor do raio da circunferência: "))
altura = float(input("Digite o valor da altura do cilíndro: "))
areacircun = pi * (raio*raio)
volume = areacircun * altura
print(f"O volume do cilíndro é: {volume:.2f}")