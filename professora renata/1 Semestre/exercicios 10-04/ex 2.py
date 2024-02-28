import random
from random import randint
n=[]
par=0
for i in range(20):
    n.append(randint(1,50))
print(n)
for num in n:
    if num%2==0:
         par+=1


