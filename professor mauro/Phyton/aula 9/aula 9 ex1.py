
while True:
    num = int(input("Digite um número inteiro de 3 algarismos: "))
    if num<1000:
        centena = num // 100
        dezena = (num // 10) % 10
        unidade = num % 10
        print("Centena =", centena)
        print("Dezena =", dezena)
        print("Unidade =", unidade)

    else:
        print('Número invalido')
        


