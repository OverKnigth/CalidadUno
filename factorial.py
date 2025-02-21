import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
    inicio = time.time()
    print(factorial_iterative(20))
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio} segundos")

    inicio = time.time()
    print(factorial_recursive(20))
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio} segundos")
    