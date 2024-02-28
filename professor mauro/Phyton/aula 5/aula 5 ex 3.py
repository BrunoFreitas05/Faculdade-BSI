
v=float(input("Digite o valor da compra =>R$"))
if(v>=500):
   p25=(v*0.25)
   vr=(v-p25)
   print(f"O valor do desconto obtido foi de R${p25} E o valor final é de R$ {vr}")
elif(v>=200):
   p20=(v*0.20)
   vr2=(v-p20)
   print(f"O valor do desconto obtido foi de R$ {p20} E o valor final é de R$ {vr2}")
else:
     p15=(v*0.15)
     vr3=(v-p15)
     print(f"O valor do desconto obtido foi de R$ {p15} E o valor final é de R$ {vr3}")



