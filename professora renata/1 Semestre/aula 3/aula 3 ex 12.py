print("informe uma data")
dia= int(input("Dia -> "))
mes= int(input("Mes -> "))
ano= int(input("Ano -> "))
valida= True
if mes==2:
    if(ano%4==0 and ano% 100!=0) or ano%400==0:
        if dia<1 or dia>29:
            valida= False
elif mes in [4,6,9,11]:
    if dia<1 or dia>30:
        valida=False
elif mes in[1,3,5,7,8,10,12]:
    if dia<1 or dia>31:
        valida=False
else:
    valida=False
if valida:
    print('Data Valida')
else:
    print("Dara invalida")


