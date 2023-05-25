while True:
    inicio = int(input("Bem-vindo ao site de cálculo de prestações (digite 1 para continuar): "))
    if inicio == 1:
        break
valor = int(input("Digite o valor do capital inicial: "))
tempo = int(input("Digite o valor do tempo: "))
taxa = int(input("Digite o valor da taxa: "))
taxafinal = taxa / 100
prestacao = valor + (valor*taxafinal*tempo)
print(f"O valor da prestação é: {prestacao}")