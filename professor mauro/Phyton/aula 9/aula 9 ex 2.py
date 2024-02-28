while True:
    vp=int(input('Digite a velocidade maxima permitida-> '))
    vel=int(input('Digite qual a sua velocidade-> '))
    if vp<vel:
        m=vel-vp
        print(f'Seu Veiculo está {m} km acima da velocidade permitida ')
    else:
        print('Seu veiculo esta dentro da velocidade permitida')

