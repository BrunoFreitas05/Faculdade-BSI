from random import randint
a=[]
for i in range(10):
    a.append(randint(1,50))
print("Números gerados: ", *a)
la=sorted(a)
print("Organizada em ordem crescente", *la)