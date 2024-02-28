a=[0]*10
print("Digite os valores de A: ")
for i in range(10):
    a[i]=int(input())
maior=a[0]
menor=a[0]
for i in range(1,10):
    if (a[i]>maior):
        maior=a[i]
    elif (a[i]<menor):
        menor=a[i]
print(f"Maior valor = {maior} ")
print(f"Menor valor = {menor} ")


