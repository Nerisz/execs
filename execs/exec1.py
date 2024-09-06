def is_fibonacci_number(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

numero = int(input("Informe um número para verificar: "))

if is_fibonacci_number(numero):
    print(f"{numero}, este é um número Fibonacci.")
else:
    print(f"{numero}, este não é um número Fibonacci.")