a=[0]*5
for i in range(5):
    a[i]=[0]*5
    for j in range(5):
        a[i][j]=i*j
print("Matriz:")
for i in range(5):
    print(a[i])