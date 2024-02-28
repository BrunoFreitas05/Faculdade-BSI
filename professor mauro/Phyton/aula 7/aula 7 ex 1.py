
while True:
    n = float(input("Digite a nota-> "))
    if n<0 or n>10:
        print('Nota invalida!')
    else:
        print(f'Nota= {n}')
        break
