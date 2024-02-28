import random

numeros=[]
i=0
while i<=20:
    numeros.append(random.randint(1, 50))
    i+=1
maior=max(numeros)
menor=min(numeros)
print(f"Números gerados{numeros}")
print(f" menor valor é {menor}")
print(f" maior valor é {maior}")
