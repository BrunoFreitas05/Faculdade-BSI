a=0
b=1
n=int(input("Informe quantos termos deseja da sequencia de Fibonacc: "))
print("1", end =" ")
for i in range(1,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c