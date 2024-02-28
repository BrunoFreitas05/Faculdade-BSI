def isprimo(n):
    if -1<=n<=1:
        return False
    for d in range(2,n):
        if n%d==0:
            return False
    return True
numero=int(input())    
if isprimo(numero):
    print(f'{numero} é um numero primo')
else:
    print(f'{numero} nao é um numero primo')



  
