def is_prime(n: int) -> bool:
    """Comprueba si un entero n es primo (los menores que 2 no lo son)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_list(limit: int) -> list[int]:
    """Genera una lista de números primos hasta limit (incluido)."""
    if limit < 2:
        return []
    return [i for i in range(2, limit + 1) if is_prime(i)]


def check_palindrome(primes: list[int]) -> list[int]:
    """Devuelve los números primos de la lista que son palíndromos."""
    return [i for i in primes if str(i) == str(i)[::-1]]


def categorize_prime(prime: int) -> str:
    """Clasifica un número primo en 'pequeños', 'medianos' o 'grandes'."""
    if prime < 10:
        return "pequeños"
    if prime < 100:
        return "medianos"
    return "grandes"


def main() -> None:
    for n in [-5, 0, 1, 2, 3, 4, 17, 25, 101]:
        print(f"is_prime({n}) -> {is_prime(n)}")

    print("\nprimos hasta 1:", prime_list(1))
    primos = prime_list(150)
    print("primos hasta 150:", primos)

    palindromos = check_palindrome(primos)
    print("\nprimos palíndromos hasta 150:", palindromos)

    print("\nclasificación de muestras:")
    for p in [3, 13, 131]:
        print(f"{p} -> {categorize_prime(p)}")


if __name__ == "__main__":
    main()