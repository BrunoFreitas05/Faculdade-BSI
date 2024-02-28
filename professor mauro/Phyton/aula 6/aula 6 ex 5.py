num=int(input('Digite um numero: '))
inv=0
while num>0:
    dig=num%10
    inv=inv*10+dig
    num=num//10
print(f'o número inverso é igual a {inv}' )