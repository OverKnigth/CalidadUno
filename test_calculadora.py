import pytest
from calculadora import suma, division

@pytest.mark.parametrize("a, b, esperado", [(2, 3, 5), (-1, -1, -2), (0, 0, 0)])
def test_suma(a, b, esperado):
    assert suma(a, b) == esperado

def test_division():
    assert division(4, 2) == 2
    assert division(-5, 4) == -1.25
    with pytest.raises(ValueError):
        division(10, 0)

