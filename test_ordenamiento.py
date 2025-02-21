import pytest
from ordenamiento import bubble_sort, seleccion_sort, insertion_sort


def test_bubble_sort():
    arr = [987654, 123456, 654321, 111222, 999999]
    assert bubble_sort(arr[:]) == [111222, 123456, 654321, 987654, 999999]

    arr = [45, -12, 78, -5, 23, -9]
    assert bubble_sort(arr[:]) == [-12, -9, -5, 23, 45, 78]

    arr = [3.14, 1.41, 2.71, 0.99, 4.56]
    assert bubble_sort(arr[:]) == [0.99, 1.41, 2.71, 3.14, 4.56]


def test_seleccion_sort():
    arr = [-10, -5, -20, 0, 10]
    assert seleccion_sort(arr[:]) == [-20, -10, -5, 0, 10]

    arr = [1000000000, 999999999, 1000000001, 1000000002]
    assert seleccion_sort(arr[:]) == [999999999, 1000000000, 1000000001, 1000000002]

    arr = [50, 40, 30, 20, 10]
    assert seleccion_sort(arr[:]) == [10, 20, 30, 40, 50]


def test_insertion_sort():
    arr = [-50, 20, -30, 10, -10]
    assert insertion_sort(arr[:]) == [-50, -30, -10, 10, 20]

    arr = [0, 0, 0, 0, 0]
    assert insertion_sort(arr[:]) == [0, 0, 0, 0, 0]

    arr = [3, 2.5, 5, 1.7, 4]
    assert insertion_sort(arr[:]) == [1.7, 2.5, 3, 4, 5]
