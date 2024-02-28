def contar_diferencas(palavra1, palavra2):
    return sum(p1 != p2 for p1, p2 in zip(palavra1, palavra2))

def encontrar_correspondencia(palavra):
    palavras_corretas = ["one", "two", "three"]
    erros_permitidos = 1

    for i, palavra_correta in enumerate(palavras_corretas):
        if contar_diferencas(palavra, palavra_correta) <= erros_permitidos:
            return i + 1  # Adiciona 1 para corresponder aos valores numéricos

    return 0

def main():
    num_palavras = int(input("Quantas palavras você deseja verificar? "))
    resultados = []

    for _ in range(num_palavras):
        palavra = input("Digite uma palavra em minúsculas: ").strip()
        resultado = encontrar_correspondencia(palavra)
        resultados.append(resultado)

    print("Valores numéricos das palavras:")
    for valor in resultados:
        print(valor)

if __name__ == "__main__":
    main()
