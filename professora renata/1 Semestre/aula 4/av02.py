n=int(input("Digite o valor inicial "))
for i in range(n):
    x=int(input("Digite outro valor "))
    vi=x
    pares=0
    impares=1
    maximo=x
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            pares += 1
        else:
            x = 3 * x + 1
            impares +=1
        if x > maximo:
            maximo=x
    print("Valor inicial:", vi)
    print("Numeros Pares:", pares)
    print("Numeros Impares:", impares)
    print("Maior Numero:", maximo)