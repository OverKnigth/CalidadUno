import pytest
from busqueda import busqueda_lineal, busqueda_binaria_iterativa, busqueda_binaria_recursiva

@pytest.mark.parametrize("arr, x, esperado", [
    ([64, 34, 25, 12, 22, 11, 90], 22, 4),
    ([10, 20, 30, 40, 50], 30, 2),
    ([5, 1, 7, 9, 3], 9, 3),
    ([1, 2, 3, 4, 5], 6, -1)  
])
def test_busqueda_lineal(arr, x, esperado):
    assert busqueda_lineal(arr, x) == esperado

@pytest.mark.parametrize("arr, x, esperado", [
    ([11, 12, 22, 25, 34, 64, 90], 22, 2),
    ([1, 3, 5, 7, 9], 7, 3),
    ([10, 20, 30, 40, 50], 25, -1)  
])
def test_busqueda_binaria_iterativa(arr, x, esperado):
    assert busqueda_binaria_iterativa(arr, x) == esperado

@pytest.mark.parametrize("arr, x, esperado", [
    ([11, 12, 22, 25, 34, 64, 90], 22, 2),
    ([1, 3, 5, 7, 9], 9, 4),
    ([10, 20, 30, 40, 50], 60, -1)  
])
def test_busqueda_binaria_recursiva(arr, x, esperado):
    assert busqueda_binaria_recursiva(arr, x, 0, len(arr) - 1) == esperado