num=int(input("Digite um numero para calculo ao quadrado-> "))
soma=0
impar=1
for i in range(num):
    soma+=impar
    impar+=2
print(f"{num} ao quadrado é {soma}")

