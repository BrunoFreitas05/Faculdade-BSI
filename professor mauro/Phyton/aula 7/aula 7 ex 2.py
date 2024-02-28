
soma=0
cont=0
while True:
    id=int(input("Digite a idade-> "))
    if id>0:
        soma+=id
        cont+=1
    else:
        break
if cont==0:
    print("Não houve idades digitadas!")
else:
    med=soma/cont
    print(f"Media das idades = {med:.0f}")





