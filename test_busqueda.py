import pytest
from busqueda import busqueda_lineal, busqueda_binaria_iterativa, busqueda_binaria_recursiva

@pytest.mark.parametrize("arr, x, esperado", [
    ([64, 34, 25, 12, 22, 11, 90], 22, 4),
    ([50, 30, 10, 70, 20], 10, 2),
    ([5, 3, 8, 1, 6], 3, 1),
    ([1, 2, 3, 4, 5], 6, -1)  
])
def test_busqueda_lineal(arr, x, esperado):
    assert busqueda_lineal(arr, x) == esperado

@pytest.mark.parametrize("arr, x, esperado", [
    ([11, 12, 22, 25, 34, 64, 90], 22, 2),
    ([2, 4, 6, 8, 10], 6, 2),
    ([3, 5, 7, 9, 11], 8, -1),
    ([1, 3, 5, 7, 9], 7, 3)  
])
def test_busqueda_binaria_iterativa(arr, x, esperado):
    assert busqueda_binaria_iterativa(arr, x) == esperado

@pytest.mark.parametrize("arr, x, esperado", [
    ([11, 12, 22, 25, 34, 64, 90], 22, 2),
    ([3, 5, 7, 9, 11], 5, 1),
    ([20, 40, 60, 80, 100], 60, 2),
    ([10, 20, 30, 40, 50], 60, -1)  
])
def test_busqueda_binaria_recursiva(arr, x, esperado):
    assert busqueda_binaria_recursiva(arr, x, 0, len(arr) - 1) == esperado
