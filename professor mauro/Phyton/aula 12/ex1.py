from random import randint

a=[0]*5
for i in range(5):
    a[i]= [0]*5
    for j in range(5):
        a[i][j]=(randint(1,50))
    print(a[i])

print("Diagonal Secundaria")
for i in range(5):
    for j in range(5):
        if (i+j==4):
            print(a[i][4-i])





