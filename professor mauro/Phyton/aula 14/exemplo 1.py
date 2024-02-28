def troco(n):
    moedas=[100,25,10,5,1]
    total=0
    for i in range(len(moedas)):
        num_moedas=n//moedas[i]
        n-=num_moedas*moedas[i]
        total+=num_moedas
    return total
