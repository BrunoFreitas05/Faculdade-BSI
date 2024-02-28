n=int(input('Digite um número com 3 algarismos-> '))
if n>1000:
    print('Numero invalido')
else:
    c=n//100
    d=(n%100)//10
    u=n%10
if c<d and d<u:
    print('seu número é ascendente')
else:
    print('Seu numero nao é ascendente')





