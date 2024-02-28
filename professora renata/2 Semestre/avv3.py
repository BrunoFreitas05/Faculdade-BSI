
def ler_informacoes_candidatos():
    n = int(input())
    candidatos = [input() for _ in range(n)]
    votos = [int(input()) for _ in range(n)]
    votos_brancos = int(input())
    votos_nulos = int(input())
    return candidatos, votos, votos_brancos, votos_nulos


def calcular_total_votos_validos(votos):
    return sum(votos)


def determinar_resultado(candidatos, votos, votos_brancos, votos_nulos):
    total_votos_validos = calcular_total_votos_validos(votos)
    metade_votos_validos = total_votos_validos / 2
    indice_vencedor = votos.index(max(votos))
    
    if votos[indice_vencedor] > metade_votos_validos:
        return f"{candidatos[indice_vencedor]} foi o vencedor da eleição", total_votos_validos
    else:
        candidatos_votos_ordenados = sorted(zip(candidatos, votos), key=lambda x: x[1], reverse=True)
        segundo_turno = f"Haverá segundo turno entre:\n{candidatos_votos_ordenados[0][0]}\n{candidatos_votos_ordenados[1][0]}"
        return segundo_turno, total_votos_validos


def main():
    candidatos, votos, votos_brancos, votos_nulos = ler_informacoes_candidatos()
    resultado, total_votos = determinar_resultado(candidatos, votos, votos_brancos, votos_nulos)
    
    print(resultado)
    print(f"Total de votos: {total_votos + votos_brancos + votos_nulos}")
    print(f"Votos válidos: {total_votos}")

if __name__ == "__main__":
    main()
