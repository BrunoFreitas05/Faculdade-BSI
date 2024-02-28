i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))
qn = int(input("Digite a quantidade de números múltiplos desejada: "))

numeros = []
contador = 0
numero = 0

while contador < qn:
    if numero % i == 0 or numero % j == 0:
        numeros.append(numero)
        contador += 1
    numero += 1

print("Os primeiros", qn, "números múltiplos de", i, "ou", j, "ou ambos são:")
for numero in numeros:
    print(numero, end=" ")