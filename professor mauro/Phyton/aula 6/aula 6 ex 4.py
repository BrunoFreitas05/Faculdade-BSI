num=int(input("Digite um número: "))
alg=0
while num>0:
    num//=10
    alg+=1
print(f'o número tem {alg} algarismos')