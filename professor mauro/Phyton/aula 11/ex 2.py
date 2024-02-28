from random import randint
a=[]
b=[]
for i in range(20):
    a.append(randint(1,50))
print("Números gerados: ", *a)
for i in range(20):
    b.insert(0,a[i])
print("Lista invertida:",*b)
