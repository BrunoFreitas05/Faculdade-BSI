a=int(input('Digite o primeiro valor-> '))
b=int(input('Digite o segundo valor-> '))
c=int(input('Digite o terceiro valor-> '))
if(a>b or a>c):
    if(b<c):
       a,b=b,a
else:
    a,c=c,a
if(b>c):
    b,c=c,b
    print(f"A= {a} B= {b} C= {c}")
