# inputs iniciais
posInicialLinha = int(input('Em qual linha será a posição inicial? (max=20) '))
posInicialColuna = int(input('Em qual coluna será a posição inicial? (max=20) '))

# criando matriz 20x20 cheia de "."
A = []
for i in range(20):
    L = []
    for j in range(20):
        L.append('.')
    A.append(L)

# marcando a posição inicial na matriz
A[posInicialLinha][posInicialColuna] = '+'

F = True
while F:
    resposta = input('Escolha uma opção: (N) (S) (L) (O) (A) (F): ')

    if resposta == 'N':
        casas = int(input('Quantas "casas" irá se movimentar para o Norte? '))
        for i in range(1, casas + 1):
            if A[posInicialLinha - i][posInicialColuna] != '#':
                A[posInicialLinha - i][posInicialColuna] = '+'

        posInicialLinha -= casas

    elif resposta == 'S':
        casas = int(input('Quantas "casas" irá se movimentar para o Sul? '))
        for i in range(1, casas + 1):
            if A[posInicialLinha + i][posInicialColuna] != '#':
                A[posInicialLinha + i][posInicialColuna] = '+'

        posInicialLinha += casas

    elif resposta == 'L':
        casas = int(input('Quantas "casas" irá se movimentar para o Leste? '))
        for i in range(1, casas + 1):
            if A[posInicialLinha][posInicialColuna + i] != '#':
                A[posInicialLinha][posInicialColuna + i] = '+'

        posInicialColuna += casas

    elif resposta == 'O':
        casas = int(input('Quantas "casas" irá se movimentar para o Oeste? '))
        for i in range(1, casas + 1):
            if A[posInicialLinha][posInicialColuna - i] != '#':
                A[posInicialLinha][posInicialColuna - i] = '+'

        posInicialColuna -= casas

    elif resposta == 'A':
        A[posInicialLinha][posInicialColuna] = '#'

    elif resposta == 'F':
        F = False

    else:
        print('\nResposta inválida. Tente novamente.\n')

# exibindo a matriz resultante
for linha in A:
    for elemento in linha:
        print(elemento, end=' ')
    print()
