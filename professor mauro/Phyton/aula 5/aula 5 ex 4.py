p=float(input("Digite qual o seu peso-> "))
a=float(input('Digite qual a sua altura-> '))
imc=p/a**2
if(imc<18):
    print(f'Abaixo do Peso. IMC= {imc:.0f}')
elif(imc<25):
     print(f"Peso Normal. IMC= {imc:.0f}")
elif(imc<30):
    print(f"Acima do Peso. IMC= {imc:.0f}")
else:
    print(f"Obesidade. IMC= {imc:.0f}")