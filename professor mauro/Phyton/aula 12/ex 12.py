A=[]*5
for i in range(5):
    A[i]=[0]*5
    for j in range(5):
        A[i][j]=int(input())
id=True
for i in range(5):
    for j in range(5):
        if((i==j and A[i][j]!=1)or (i!=j and A[i][j]!=0)):
            id=False
            break
if id:
    print("Matriz é identidade!")
else:
    print("Matriz nao é identidade")
