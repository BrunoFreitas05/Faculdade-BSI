id=int(input('Digite qual a sua idade:'))
if(id<=8):
    print("Categoria infantil A")
elif(id<13):
    print("Categoria infantil B")
elif(id<18):
    print("Categoria Juvenil A")
elif(id<21):
    print("Categoria Juvenil B")
else:
    print("Categoria Senior")
