from random import randint
a=[]
b=[]
for i in range(10):
    a.append(randint(1,50))
print("Números gerados: ", *a)
for i in range(10):
    b.append(randint(1,50))
print("Números gerados: ", *b)
c=[]
c=a[ : ]
for val in b:
    if val not in a:
        c.append(val)
print("Uniao de A com B=", c)

