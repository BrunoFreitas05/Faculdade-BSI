a=int(input("Digite a temperatura do primeiro dia-> "))
b=int(input("Digite a temperatura do segundo dia-> "))
c=int(input("Digite a temperatura do terceiro dia-> "))
if b<a and b<=c:
    print(":)")
elif b>a and b>=c:
    print(":(")
elif a<b and b<c and c-b<b-a:
    print(":(")
elif a<b and b<c and c-b>=b-a:
    print(":)")
elif a>b and b>c and b-c<a-b:
    print(":)")
elif a>b and b>c and b-c>=a-b:
    print(":(")
elif a==b and b<c:
    print(":)")
elif a==b and b>=c:
    print(":(")





