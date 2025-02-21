import time
import numpy as np

def get_first_element(arr):
    return arr[0]

def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def busqueda_binaria(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1    

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

np.random.seed(42)
arr = np.random.randint(1, 100, size=1000)

inicio = time.time()
arr.sort()
print(get_first_element(arr))
fim = time.time()
print(f"Tiempo de ejecución: {fim - inicio} segundos")

inicio = time.time()
print(busqueda_lineal(arr, 100))
fim = time.time()
print(f"Tiempo de ejecución: {fim - inicio} segundos")