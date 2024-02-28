s=float(input("Digite o seu salario: R$"))
p=float(input("Digite o valor da prestação: R$"))
p20=s*0.2
if p>p20:
    print("Emprestimo Não Concedido!")
else:
    print("Emprestimo Concedido!")