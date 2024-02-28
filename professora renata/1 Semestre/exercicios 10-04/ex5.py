from random import randint
l=[]
for i in range(10):
    l.append(randint(1,50))
print("Números Gerados ->", *l)

print("Ordem inversa-> ",end="")
for i in range(9,-1,-1):
    print(l[i], end=" ")



l=[]
for i in range(10):
    l.append(randint(1,50))
print("Números Gerados ->", *l)
print(l[::-1])




