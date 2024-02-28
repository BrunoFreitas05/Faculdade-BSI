A=[0]*8
CL=int(input("Digite a linha inicial da Torre: "))
CC=int(input("Digite a Coluna Inicial: "))
for i in range(8):
    A[i]= [0]*8
for i in range(8):
    A[CL][i]=1
    A[i][CC]=1
for i in range(8):
    print(A[i])
