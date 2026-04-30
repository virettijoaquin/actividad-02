import pytest
from app.puntos import calcular_puntos


# TC01 - Caso exitoso
def test_calculo_puntos_platinum():
    resultado = calcular_puntos(10000, "platinum")
    assert resultado == 500


# TC02 - Caso de error
def test_monto_negativo():
    with pytest.raises(ValueError):
        calcular_puntos(-5000, "gold")


# TC03 - Caso borde
def test_monto_cero():
    resultado = calcular_puntos(0, "black")
    assert resultado == 0