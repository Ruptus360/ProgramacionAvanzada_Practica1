def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


def leap_years_between(start,end):
    bisiesto = []
    for i in range(start,end+1):
        if is_leap_year(i):
            bisiesto.append(i)
    return bisiesto

def explain_leap_year(year: int) -> str:
    if year % 400 == 0:
        return f"{year} es bisiesto porque es divisible entre 400."
    if year % 100 == 0:
        return f"{year} no es bisiesto porque es divisible entre 100 pero no entre 400."
    if year % 4 == 0:
        return f"{year} es bisiesto porque es divisible entre 4 y no entre 100."
    return f"{year} no es bisiesto porque no es divisible entre 4."

def main() -> None:
    while True:
        cadena = int(input("Introduce un año: "))
        try:
            year = cadena
            break
        except ValueError:
            print("Introduce un año entero válido.")

    if year < 1582:
        print("El calendario gregoriano aún no existía en ese año.")
    else:
        print(explain_leap_year(year))


if __name__ == "__main__":
    main()