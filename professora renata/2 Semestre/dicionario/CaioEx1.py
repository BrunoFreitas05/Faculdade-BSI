# Função principal
def main():
    # Transações de exemplo
    transacoes_exemplo = ["C 700.00", "D 100.00", "C 350.00", "D 123.00", "D 75.00"]

    # Nome do arquivo
    arquivo_nome = "contacorrente.txt"

    try:
        # Criar o arquivo e escrever as transações
        with open(arquivo_nome, 'w') as arquivo:
            for transacao in transacoes_exemplo:
                arquivo.write(transacao + '\n')

        print(f"Arquivo '{arquivo_nome}' criado com sucesso!")

        # Ler as transações do arquivo
        with open(arquivo_nome, 'r') as arquivo:
            linhas = arquivo.readlines()

        # Processar as transações
        transacoes = [linha.strip() for linha in linhas]

        # Calcular o saldo final
        saldo_final = calcular_saldo_final(transacoes)

        # Imprimir as informações
        print("\nInformações das transações:")
        for transacao in transacoes:
            print(transacao)

        print("\nSaldo Final: R$ {:.2f}".format(saldo_final))

    except Exception as e:
        print(f"Erro: {e}")

# Chamar a função principal
if __name__ == "__main__":
    main()

