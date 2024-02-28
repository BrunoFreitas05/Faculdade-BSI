from random import randint
a=[]
p=[]
im=[]
for i in range(20):
    a.append(randint(1,50))
print("Números gerados: ", *a)
for i in range(20):
    if (a[i]%2==0):
        p.append(a[i])
    else:
        im.append(a[i])
if len(p)>0:
    print("Pares:", p)
if len(im)>0:
    print("Impares:", im)




