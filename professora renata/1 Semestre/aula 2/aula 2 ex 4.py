conta=float(input('informe o valor da conta -> R$'))
individual=int(conta)//3
felipe=conta-2*individual
print(f'A conta será dividida assim:'
      f'\nCarlos - R${individual:.2f}'
      f'\nAndre - R${individual:.2f}'
      f'\nFelipe - R${felipe:.2f}')
