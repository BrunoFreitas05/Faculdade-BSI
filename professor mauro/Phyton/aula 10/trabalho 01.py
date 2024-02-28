a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if b > a:
    print("O valor de B não pode ser maior que A.")
else:
    v = 0
    t= b
    while t > 0:
        t //= 10
        v += 1

    if b == a % (10 ** v):
        print(f"{a} termina com {b}")
    else:
        print(f"{a} não termina {b}")