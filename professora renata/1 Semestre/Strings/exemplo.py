nota=input("Qual a nota: ")
print(nota)
if nota.replace('.','').isdigit():
    nota=float(nota)
