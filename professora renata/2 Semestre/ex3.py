qtd_linhas = int(input("Digite a quantidade de linhas: "))
tipo_letra = input("Digite 'maiuscula'ou'minuscula' : ")

for i in range(qtd_linhas):
    linha = ""
    for j in range(qtd_linhas - i - 1):
        linha += ".."
    for k in range(i + 1):
        if tipo_letra.lower() == "maiuscula":
            linha += chr(65 + k)
        else:
            linha += chr(97 + k)
    print(linha.rjust(qtd_linhas*2-1))