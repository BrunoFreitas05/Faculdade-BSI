from random import randint
l=[]
for i in range(10):
    l.append(randint(1,50))
print("Números Gerados ->", *l)
l.sort(reverse=True)
print("Numeros ordenados->", l)