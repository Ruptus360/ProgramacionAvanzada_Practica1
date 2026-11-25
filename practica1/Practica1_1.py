"""comprobacion de cadena Booleana"""

def is_integer(cadena: str = "") -> bool: 
    try:
        int(cadena)
        return True
    except ValueError:
        return False


"""Dividion entera, acumulacion del resto y cambio de unidad"""

def seconds_todhms(segundos: int = 0) -> tuple[int, int, int, int]:
    if segundos < 0:
        raise ValueError("Solo valores no negativos")

    dias = segundos // 86_400
    resto = segundos % 86_400

    horas = resto // 3_600
    resto = resto % 3_600

    minutos = resto // 60
    seg_restantes = resto % 60

    return dias, horas, minutos, seg_restantes
        


def main() -> None:
    while True:
        cadena = input("Introduce los segundos: ")

        if not is_integer(cadena):
            print("No es un entero válido")
            continue

        segundos = int(cadena)

        try:
            resultado = seconds_todhms(segundos)
        except ValueError:
            print("Solo positivos")
            continue

        print(resultado)
        break







if __name__ == "__main__":
    main()