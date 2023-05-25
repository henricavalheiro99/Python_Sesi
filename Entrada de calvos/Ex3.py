while True:
    inicio = int(input("Bem-vindo ao site de  sucessor e antecessor (digite 1 para continuar): "))
    if inicio == 1:
        break
num = int(input("Digite um número: "))
antecessor = num -1
sucessor =  num +1
print(f"O antecessor e o sucessor de {num} são, respectivamente, {antecessor} e {sucessor}")