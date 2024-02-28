
n = int(input())

candidatos = [input() for _ in range(n)]
votos = [int(input()) for _ in range(n)]
votos_brancos = int(input())
votos_nulos = int(input())
total_votos_validos = sum(votos)
metade_votos_validos = total_votos_validos / 2
indice_vencedor = votos.index(max(votos))

if votos[indice_vencedor] > metade_votos_validos:
    print(f"{candidatos[indice_vencedor]} foi o vencedor da eleição")
else:
    candidatos_votos_ordenados = sorted(zip(candidatos, votos), key=lambda x: x[1], reverse=True)
    print("Haverá segundo turno entre:")
    print(candidatos_votos_ordenados[0][0])
    print(candidatos_votos_ordenados[1][0])

print(f"Total de votos: {total_votos_validos + votos_brancos + votos_nulos}")
print(f"Votos válidos: {total_votos_validos}")
