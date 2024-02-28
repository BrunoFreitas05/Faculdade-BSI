sp=si=0
c=1
while c<=10:
    num=int(input(f"informe o{c} número => "))
    if num%2==0:
        sp+=num
    else:
        si+=num
    c+=1
print(f"A soma dos números pares é {sp}"
      f" e a soma dos números ímpares é {si}")