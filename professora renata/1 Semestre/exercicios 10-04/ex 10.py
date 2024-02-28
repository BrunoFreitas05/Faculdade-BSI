from random import randint
l=[]
while len(l)!=10:
    x=randint(1,50)
    print(x,end=" ")
    if x not in l:
        l.append(x)
l.sort()
print("\n Numeros Gerados ->",l)