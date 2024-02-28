a=int(input("Digite o primeiro angulo do triangulo: "))
b=int(input("Digite o segundo angulo do triangulo: "))
c=int(input("Digite o terceiro angulo do triangulo: "))
soma=a+b+c
if soma!=180:
    print("Não é triangulo")
elif a==90 or b==90 or c==90:
    print("Triângulo retângulo")
elif a>90 or b>90 or c>90:
    print("Triângulo obtusângulo")
else:
    print("Triângulo acutângulo")