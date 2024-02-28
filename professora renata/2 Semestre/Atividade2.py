
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def acm_to_decimal(acm):
    decimal = 0
    n = len(acm)
    
    for i in range(n):
        digit = int(acm[i])
        decimal += digit * fatorial(n - i)
    
    return decimal

while True:
    acm = input()
    if acm == "0":
        break
    decimal = acm_to_decimal(acm)
    print(decimal)
