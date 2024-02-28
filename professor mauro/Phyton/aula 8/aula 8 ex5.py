num=int(input("Digite um número-> "))
soma=0
for div in range(1,num//2+1):
    if num%div==0:
        soma+=div
if soma==num:
    print(f"O Número {num} é perfeito")
else:
    print(f"O Número {num} nao é perfeito")
