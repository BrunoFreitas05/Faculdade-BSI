for n in range(1000,10000):
    p1=n//100
    p2=n%100
    if(p1+p2)**2==n:
        print(n)