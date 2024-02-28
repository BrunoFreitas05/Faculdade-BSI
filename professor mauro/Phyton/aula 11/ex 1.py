from random import randint
a=[]
for i in range(20):
    a.append(randint(1,50))
print("Números gerados: ", *a)
for i in range(10):
    a[i],a[i+10]=a[i+10],a[i]
print("Valor modificado:")
print(a)