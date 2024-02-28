def fatorial(n):
    if n==1:
        return 1
    return n* fatorial(n-1)

num=int(input('Entre com um valor -> '))
print(f'Fatorial de {num} é {fatorial(num)}')
