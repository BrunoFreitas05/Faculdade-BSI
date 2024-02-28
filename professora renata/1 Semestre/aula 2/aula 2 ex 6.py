dist=float(input('Entre com a distancia ->'))
veloc=float(input('Velocidade média ->'))
tempo=dist/veloc
print(f'Levará {tempo} horas')
horas=int(tempo)
minutos=(tempo-horas)*60
print(f'Levará {horas} horas(s) e {minutos} minutos(s)')
