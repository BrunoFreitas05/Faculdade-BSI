n=int(input("Digite um numero -> "))
s=int(input("Digite o valor da soma-> "))
xi=[]
for i in range(n):
    valor=int(input("Digite os valores da lista-> "))
    xi.append(valor)
for i in range(n):
    soma=0
    for j in range(i,n):
        soma+=xi[j]
        if soma==s:
            print('Intervalo encontrado', [i+1])




