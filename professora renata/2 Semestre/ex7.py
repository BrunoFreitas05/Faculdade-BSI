def validaEntrada(d):
    if len(d)!=10:
        return False
    if not d.replace('/','').isdigit():
        return False
    if d[2]!='/' and d[5]!='/':
        return False
    return True


def validaData(d):
    dia, mes,ano= d.split('/')
    dia,mes,ano= int(dia), int(mes), int(ano)
    if mes==2:
        if anoBissexto(ano):
            if 1<dia<=29:
                return True
        else:
            if 1<=dia<=28:
                return True
    elif mes in [1,3,5,7,8,10,12]:
        if 1 <=dia<=31:
            return True
        elif mes in[4,6,9,11]:
            if 1<=dia<+30:
                return True
        return False    
        
                
def anoBissexto(a):
    if(a%4==0 and a%100 !=0) or a %400==0:
        return True
    return False



data=input('Informe a data no formato dd/mm/aaa -> ')
if validaEntrada(data):
    if validaData(data):
        print('Data Valida')
    else:
        print('Data Invalida')
else:
    print('Entrada no formato invalido')        





