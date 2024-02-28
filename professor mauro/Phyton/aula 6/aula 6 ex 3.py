a=int(input("Digite um número: "))
b=int(input("Digite outro numero: "))
soma=0
if a%2==0:
   a+=1
while a<=b:
    soma+=a
    a+=2
print(f"Soma = {soma}")


