dias=int(input('Informe quantos dias a fabrica esta sem acidentes-> '))
a=dias//365
m=dias%365//30
d=dias%365%30
print(f'A fabrica está há {a} anos, {m} meses e {d} dias sem acidentes')

