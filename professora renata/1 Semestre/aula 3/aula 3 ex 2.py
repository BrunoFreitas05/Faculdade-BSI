a=float(input('Digite o valor do primeiro lado '))
b=float(input('Digite o valor do segundo lado '))
c=float(input('Digite o valor do terceiro lado '))
if a<b+c and b<a+c and c<a+b:
    if(a==b and b==c):
        print("Triângulo equilátero")
    elif a==b or a==c or b==c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")

