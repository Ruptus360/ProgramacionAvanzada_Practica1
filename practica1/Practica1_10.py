def read_strings() -> list[str]:
    items: list[str] = []
    while True:
        try:
            n = int(input("¿Cuántas cadenas desea introducir?: ").strip())
            if n < 0:
                print("Introduce un número entero mayor o igual que 0.")
                continue
            break
        except ValueError:
            print("Introduce un número entero válido.")

    for i in range(n):
        cadena = input(f"Cadena {i + 1}: ")
        items.append(cadena)
    return items


def filter_starts_with(items: list[str]) -> None:
    letra = input("Letra inicial: ")
    if not letra:
        print("No se introdujo ninguna letra.")
        return
    objetivo = letra[0].lower()
    coincidencias = [i for i in items if i.lower().startswith(objetivo)]
    if coincidencias:
        for i in coincidencias:
            print(i)
    else:
        print("Ninguna cadena comienza con esa letra.")


def count_substring(items: list[str]) -> None:
    sub = input("Subcadena a buscar: ")
    total = sum(1 for i in items if sub in i)
    print(f"Número de cadenas que contienen '{sub}': {total}")


def min_max_length(items: list[str]) -> None:
    if not items:
        print("La lista está vacía.")
        return

    corta = items[0]
    larga = items[0]
    for i in items[1:]:
        if len(i) < len(corta):
            corta = i
        if len(i) > len(larga):
            larga = i

    print(f"Cadena más corta: '{corta}' (longitud {len(corta)})")
    print(f"Cadena más larga: '{larga}' (longitud {len(larga)})")


def check_same_object(items: list[str]) -> None:
    if len(items) < 2:
        print("Se necesitan al menos 2 cadenas en la lista.")
        return

    for i, valor in enumerate(items):
        print(f"  [{i}] -> {valor!r}")

    while True:
        try:
            idx1 = int(input("Índice de la primera cadena: ").strip())
            idx2 = int(input("Índice de la segunda cadena: ").strip())
            if 0 <= idx1 < len(items) and 0 <= idx2 < len(items):
                break
            print("Índices fuera de rango.")
        except ValueError:
            print("Introduce índices enteros válidos.")

    if items[idx1] is items[idx2]:
        print("Son el mismo objeto en memoria (is -> True).")
    else:
        print("No son el mismo objeto en memoria (is -> False).")


def check_length_over_ten(items: list[str]) -> None:
    for i in items:
        if len(i) > 10:
            print(f"Encontrada cadena con longitud mayor que 10: '{i}' ({len(i)} caracteres)")
            break
    else:
        print("Ninguna cadena tiene más de 10 caracteres.")


def main() -> None:
    items = read_strings()

    while True:
        print("\n--- MENÚ ---")
        print("1. Cadenas que comienzan con una letra")
        print("2. Contar cadenas que contienen una subcadena")
        print("3. Cadena más larga y más corta")
        print("4. Comprobar si dos cadenas son el mismo objeto (is)")
        print("5. Comprobar si alguna cadena tiene más de 10 caracteres (for...else)")
        print("6. Volver a leer la lista de cadenas")
        print("0. Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            filter_starts_with(items)
        elif opcion == "2":
            count_substring(items)
        elif opcion == "3":
            min_max_length(items)
        elif opcion == "4":
            check_same_object(items)
        elif opcion == "5":
            check_length_over_ten(items)
        elif opcion == "6":
            items = read_strings()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()