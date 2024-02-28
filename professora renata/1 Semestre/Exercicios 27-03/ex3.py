n=int(input("Digite a quantidade de linhas=> "))
for i in range(1,2*n,2):
    linha=""
    for j in range(i):
        linha+="*"
    print(linha.center(2*n-1))
