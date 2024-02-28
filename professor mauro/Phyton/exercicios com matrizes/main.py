n = int(input("Digite a quantidade de elementos: "))
soma = (n + n**3) // 2
matriz =[[0 for j in range(n)] for i in range(n)]
print("Digite os números de 1 a" ,n*n, "para preencher a matriz:")
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Digite o número da posição ({i+1},{j+1}): "))
for i in range(n):
    soma_linha = 0
    soma_coluna = 0
    for j in range(n):
        soma_linha += matriz[i][j]
        soma_coluna += matriz[j][i]
    if soma_linha != soma or soma_coluna != soma:
        print("Não é um Quadrado Mágico")
        exit()

soma_diagonal1 = 0
soma_diagonal2 = 0
for i in range(n):
    soma_diagonal1 += matriz[i][i]
    soma_diagonal2 += matriz[i][n-i-1]
if soma_diagonal1 != soma or soma_diagonal2 != soma:
    print("Não é um Quadrado Mágico")
    exit()

print("Quadrado Mágico")
for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()