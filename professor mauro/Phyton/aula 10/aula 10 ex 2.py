a=[0]*10
b=[0]*10

print("Digite os valores de A: ")
for i in range(10):
    a[i]=int(input())

print("Digite os Valores de B: ")
for i in range(10):
    b[i]=int(input())

c=[0]*10
for i in range(10):
    c[i]=a[i]+b[i]

for i in range(10):
    print(a[i],"+",b[i],"=", c[i] )






