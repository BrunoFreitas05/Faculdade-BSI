def mais6notas():
    arq = open('C:/professora renata/2 Semestre/dicionario/notas_estudantes.txt', 'r')
    for dados in arq:
        lista = dados.split()
        if len(lista) > 7:
            print(lista[0])
    arq.close()

def media():
    arq = open('C:/professora renata/2 Semestre/dicionario/notas_estudantes.txt', 'r')
    for dados in arq:
        nome, *notas = dados.split()
        notas = list(map(float,notas))
        media = sum(notas)/len(notas)
        print(f'Aluno: {nome} Média: {media:.2f}')
    arq.close()

def MaiorMenorNota():
    arq = open('C:/professora renata/2 Semestre/dicionario/notas_estudantes.txt', 'r')
    for dados in arq:
        nome, *notas = dados.split()
        notas = list(map(float, notas))
        print(f'Aluno: {nome} Maior: {max(notas)} Menor: {min(notas)}')
    arq.close()

print('Estudantes com mais de 6 notas')
mais6notas()
print('=' * 50)
print('Média dos estudantes')
media()
print('=' * 50)
print('Maior e menor nota de cada estudante')
MaiorMenorNota()