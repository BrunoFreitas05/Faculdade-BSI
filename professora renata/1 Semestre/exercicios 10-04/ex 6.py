from random import randint
A=[]
for i in range(10):
    A.append(randint(1,50))
print(A)
x=int(input("Digite um número-> "))
b=[a * x for a in A]
print(b)







