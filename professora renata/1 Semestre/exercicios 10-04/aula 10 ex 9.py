from random import randint
l=[]
for i in range(10):
    l.append(randint(1,50))
print("Números Gerados->", l )
num=int(input("Informe o valor que deseja encontrar-> "))
if num in l:
    print(f"{num} está na lista")
else:
    print(f"{num} não está na lista")