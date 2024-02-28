troco=float(input("Qual o Valor do Troco: "))
troco*=100
moedas=[100,50,25,10,5,1]
total=[]
soma=0
for i in range(6):
    m=troco//moedas[i]
    soma+=m
    total.append(m)
    troco %=moedas[i]
print("Total de Moedas: ", soma)
for i in range(6):
    print(total[i], "moedas de", moedas[i])

