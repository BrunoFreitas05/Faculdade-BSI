import random
from random import randint
n=[]
par=0
impar=1
for i in range(10):
    n.append(randint(1,50))
print(n)

for num in n:
    if num%2==0:
         par+=1
    else: impar+=1
print("Números Pares: ", par)
print("Números impares:", impar)



