import pytest
from ordenamiento import bubble_sort, seleccion_sort, insertion_sort


def test_bubble_sort():
    # Caso 1: Lista normal
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort(arr[:]) == [11, 12, 22, 25, 34, 64, 90]

    # Caso 2: Lista en orden inverso
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr[:]) == [1, 2, 3, 4, 5]

    # Caso 3: Lista con elementos repetidos
    arr = [3, 1, 2, 3, 1, 2]
    assert bubble_sort(arr[:]) == [1, 1, 2, 2, 3, 3]


def test_seleccion_sort():
    # Caso 1: Lista normal
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert seleccion_sort(arr[:]) == [11, 12, 22, 25, 34, 64, 90]

    # Caso 2: Lista vacía
    arr = []
    assert seleccion_sort(arr[:]) == []

    # Caso 3: Lista con un solo elemento
    arr = [5]
    assert seleccion_sort(arr[:]) == [5]


def test_insertion_sort():
    # Caso 1: Lista ya ordenada
    arr = [1, 2, 3, 4, 5]
    assert insertion_sort(arr[:]) == [1, 2, 3, 4, 5]

    # Caso 2: Lista en orden inverso
    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr[:]) == [1, 2, 3, 4, 5]

    # Caso 3: Lista con números negativos
    arr = [3, -1, 2, -3, 1, 0]
    assert insertion_sort(arr[:]) == [-3, -1, 0, 1, 2, 3]
