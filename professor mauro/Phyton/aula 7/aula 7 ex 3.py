quant=0
soma=0
while True:
    p=float(input("Digite o preço do produto-> R$ "))
    if p>0:
        qp=float(input('Digite a quantidade do produto-> '))
        total=p*qp
        soma+=total
        quant+=qp
    else:
        break
print(f"Total gasto=R$ {soma}")
print(f"Total de Produtos Comprados -> {quant}")




