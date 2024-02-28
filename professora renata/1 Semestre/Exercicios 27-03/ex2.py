n=int(input("Digite a quantidade de linhas=> "))
for i in range(1,2*n):
    if i<n:
        for j in range(i):
            print("*",end="")
    else:
        for j in range(2*n-i,0,-1):
            print("*",end="")
    print()






