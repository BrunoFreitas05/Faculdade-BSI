n=int(input("Informe o número para verificar se é primo-> "))
primo=True
if -1<=n<=1:
    primo=False
else:
    for div in range(2,n):
        if n%div==0:
            primo=False
            break
if primo:
    print(f"{n} é um primo")
else:
    print(f"{n} não é um primo")