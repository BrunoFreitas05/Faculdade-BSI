for num in range(100,1000):
    n1=num//100
    n2=(num//10)%10
    n3=num%10
    soma= (n1** 3) + (n2** 3) + (n3** 3)
    if soma== num:
     print(num)