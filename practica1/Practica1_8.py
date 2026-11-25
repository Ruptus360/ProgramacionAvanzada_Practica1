def read_numbers():
    numbers = []
    while True:
        try:
            n = int(input("¿Cuántos números enteros desea introducir?: ").strip())
            if n < 0:
                print("Introduce un número entero mayor o igual que 0.")
                continue
            break
        except ValueError:
            print("Error: introduzca un número entero válido.")

    for i in range(n):
        while True:
            try:
                value = int(input(f"Número {i + 1}: ").strip())
                numbers.append(value)
                break
            except ValueError:
                print("Error: introduzca un número entero válido.")

    return numbers


def total_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


def positive_negative_sums(numbers):
    pos_sum = 0
    neg_sum = 0
    for i in numbers:
        if i > 0:
            pos_sum += i
        elif i < 0:
            neg_sum += i
    return pos_sum, neg_sum


def min_max_numbers(numbers):
    if not numbers:
        return None, None

    minimum = numbers[0]
    maximum = numbers[0]
    for i in numbers[1:]:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return minimum, maximum


def all_unique(numbers):
    seen = []
    for i in numbers:
        if i in seen:
            return False
        seen.append(i)
    return True


def compare_pos_neg_count(numbers):
    pos_count = 0
    neg_count = 0
    for i in numbers:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_count += 1

    message = (
        "Hay más números positivos que negativos."
        if pos_count > neg_count
        else (
            "Hay más números negativos que positivos."
            if neg_count > pos_count
            else "Hay tantos números positivos como negativos."
        )
    )
    return message


def main():
    numbers = read_numbers()

    while True:
        print("\n--- MENÚ ---")
        print("1. Suma de todos los números")
        print("2. Suma de positivos y suma de negativos por separado")
        print("3. Número máximo y mínimo")
        print("4. Comprobar si todos los números son únicos")
        print("5. Indicar si hay más positivos o negativos")
        print("6. Volver a leer la lista de números")
        print("0. Salir")
        option = input("Elija una opción: ").strip()

        if option == "1":
            print("Suma total:", total_sum(numbers))

        elif option == "2":
            pos_sum, neg_sum = positive_negative_sums(numbers)
            print("Suma de positivos:", pos_sum)
            print("Suma de negativos:", neg_sum)

        elif option == "3":
            minimum, maximum = min_max_numbers(numbers)
            if minimum is None or maximum is None:
                print("La lista está vacía: no hay máximo ni mínimo.")
            else:
                print("Mínimo:", minimum)
                print("Máximo:", maximum)

        elif option == "4":
            if all_unique(numbers):
                print("Todos los números de la lista son únicos.")
            else:
                print("Existen números repetidos en la lista.")

        elif option == "5":
            print(compare_pos_neg_count(numbers))

        elif option == "6":
            numbers = read_numbers()

        elif option == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()