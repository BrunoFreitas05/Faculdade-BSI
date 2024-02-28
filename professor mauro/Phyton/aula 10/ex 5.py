from random import randint
a=[]
for i in range(10):
    a.append(randint(1,50))
print("Números gerados: ", *a)
num=int(input("Digite um número-> "))
if num in a:
    cont=0
    for item in a:
        if num==item:
            cont+=1
    print(f"O valor {num} aparece {cont} vezes na lista")
else:
    print(f"O valor {num} nao existe na lista")



