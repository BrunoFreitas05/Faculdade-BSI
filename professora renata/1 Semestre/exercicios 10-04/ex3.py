from random import randint
l=[]
for i in range(10):
    l.append(randint(1,50))
print("Números Gerados ->", *l)
print("Múltiplos de 5 -> ",end="")
for i in range(10):
    if l[i]%5==0:
        print(l[i], end=" ")

