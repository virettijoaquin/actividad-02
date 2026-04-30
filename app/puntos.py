# app/puntos.py

def calcular_puntos(monto_compra, tipo_tarjeta):
    if monto_compra < 0:
        raise ValueError("El monto no puede ser negativo")

    multiplicadores = {
        "gold": 0.047,
        "platinum": 0.05,
        "black": 0.052
    }

    if tipo_tarjeta not in multiplicadores:
        raise ValueError("Tipo de tarjeta inválido")

    return monto_compra * multiplicadores[tipo_tarjeta]