def calcular_media(saltos):
    saltos.sort(reverse=True)  
    melhores_saltos = saltos[:4]  
    media = sum(melhores_saltos) / 4.0  
    return media
dados_atletas = """Camila 6.2 6.1 6.5 6.5 6.1
João 6.4 6.5 6.6 6.5 6.4
Natália 6.0 6.0 6.1 6.2 6.3"""
nome_arquivo = 'campeonato.txt'
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(dados_atletas)
def encontrar_campeao(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    dados_atletas = [linha.split() for linha in linhas]
    resultados = {}
    for i in range(0, len(dados_atletas)):
        nome = dados_atletas[i][0]
        saltos = [float(valor) for valor in dados_atletas[i][1:]]
        media = calcular_media(saltos)
        resultados[nome] = media
    campeao = max(resultados, key=resultados.get)
    return campeao
campeao = encontrar_campeao(nome_arquivo)
print(f'O campeão é: {campeao}')