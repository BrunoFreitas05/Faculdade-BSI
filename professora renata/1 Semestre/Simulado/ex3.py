def is_kaprekar_number(n):
    square = n * n
    num_digits = 0
    temp = square

    while temp > 0:
        temp //= 10
        num_digits += 1

    for i in range(1, num_digits):
        divisor = 10 ** i
        left_part = square // divisor
        right_part = square % divisor

        if left_part + right_part == n:
            return True

    return False


# Solicita ao usuário um número inteiro não negativo
number = int(input("Digite um número inteiro não negativo (até 99): "))

if is_kaprekar_number(number):
    print(f"{number} é um número de Kaprekar.")
else:
    print(f"{number} não é um número de Kaprekar.")
