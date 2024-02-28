from random import randint
l=[]
for i in range(20):
    l.append(randint(1,50))
print(l)
m=int(input("Digite um número-> "))
print("OS Números multiplos sao: ")
for i in range(20):
    if l[i]%m==0:
        print(l[i], end=" ")


