from random import randint

a=[0]*5
for i in range(5):
    a[i]= [0]*5
    for j in range(5):
        a[i][j]=(randint(1,50))
    print(a[i])

print("Triangulo Superior Direito")
for i in range(4):
    for j in range(i+1,5):
            print(a[i][j], end=" ")
