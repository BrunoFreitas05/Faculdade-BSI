def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

# Solicita ao usuário os números de base e expoente
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a {resultado}")
