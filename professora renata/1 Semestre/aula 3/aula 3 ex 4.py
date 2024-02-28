a=int(input("Digite o primeiro numero: "))
b=int(input("Digite o segundo numero: "))
c=int(input("Digite o terceiro numero: "))
if a<b and a<c:
    menor=a
elif b<c and b<c:
    menor=b
else:
    menor=c

if a>b and a>c:
    maior=a
elif b>a and b>c:
    maior= b
else:
    maior=c
meio= a+b+c-menor-maior
print("Os Numeros em ordem crescente sao:" ,menor,meio,maior)
