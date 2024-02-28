num=float(input("Digite um numero-> "))
if num>0:
    q= num**2
    r= num**0.5
    print(f"O Quadrado de {num} é {q:.2f} ")
    print(f"a Raiz Quadrada de {num} é {r:.2f}")
else:
    print("Numero invalido")
