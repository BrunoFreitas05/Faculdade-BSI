from random import randint

a=[0]*5
for i in range(5):
    a[i]= [0]*5
    for j in range(5):
        a[i][j]=(randint(1,50))
    print(a[i])

print("Triangulo Inferior Esquerdo")
for i in range(1,5):
    for j in range(i):
        print(a[i][j], end=" ")
