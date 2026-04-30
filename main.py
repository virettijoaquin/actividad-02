# main.py

from app.puntos import calcular_puntos


def main():
    print("=== Cálculo de puntos Pasaporte Despegar ===")

    try:
        monto = float(input("Ingrese el monto de la compra: "))
        tarjeta = input("Ingrese tipo de tarjeta (gold/platinum/black): ").lower()

        puntos = calcular_puntos(monto, tarjeta)

        print(f"Puntos obtenidos: {puntos}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()