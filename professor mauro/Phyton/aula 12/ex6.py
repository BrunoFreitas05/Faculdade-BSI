from random import randint

a=[0]*4
for i in range(4):
    a[i]=[0]*6
    for j in range(6):
        a[i][j]=(randint(1,50))
t=[0]*6
for i in range(6):
    t[i]=[0]*4
    for j in range(4):
        t[i][j]=a[j][i]
print("Matriz Transposta:")
for i in range(6):
    print(t[i])
