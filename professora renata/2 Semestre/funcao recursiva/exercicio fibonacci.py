def fib(T):
    if T==1 or T==2:
        return 1
    return fib(T-1) + fib(T-2)

termo= int(input("Qual o termo da sequencia de Fibonacci? -> "))
print(fib(termo))