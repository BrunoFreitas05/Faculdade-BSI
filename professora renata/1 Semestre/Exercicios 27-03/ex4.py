for n in range(100,1000):
    c=n//100
    d=n%100//10
    u=n%10
    if n%2==0:
        print(f"{n}-{c+d+u}")
    else:
        print(f"{n}- {c*d*u}")