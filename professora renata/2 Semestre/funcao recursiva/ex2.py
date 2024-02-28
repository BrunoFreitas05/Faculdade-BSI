from random import randint

# Inicializar a lista com 10 elementos aleatórios
lista = [randint(1, 50) for _ in range(10)]

def verificar(valor, indice=0):
    if indice == len(lista):
        return False
    if lista[indice] == valor:
        return True
    return verificar(valor, indice + 1)

# Valor que desejamos buscar na lista
valor_buscado = int(input("Digite o valor que deseja buscar: "))

# Chamar a função de busca recursiva
encontrado = verificar(valor_buscado)

# Exibir o resultado
if encontrado:
    print(f"O valor {valor_buscado} está contido na lista.")
else:
    print(f"O valor {valor_buscado} não está contido na lista.")
