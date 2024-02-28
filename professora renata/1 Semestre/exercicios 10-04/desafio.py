from random import randint
from time import time
tam=10
l=[]
for i in range(tam):
    l.append(randint(1,tam))
m=l.copy()
inicio=time()
fim=time()
l.sort()
print("Tempo de ordenaçao pelo metodo sort() ->", fim-inicio)

