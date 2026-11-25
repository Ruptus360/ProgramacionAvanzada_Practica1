def remove_duplicates(numbers: list[int]) -> list[int]:
    result: list[int] = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result


def rotate_left(numbers: list[int], k: int) -> list[int]:
    n = len(numbers)
    if n == 0:
        return []
    shift = k % n
    result: list[int] = []
    for i in range(n):
        result.append(numbers[(i + shift) % n])
    return result


def split_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    evens: list[int] = []
    odds: list[int] = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    merged: list[int] = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1
    return merged


def second_largest(numbers: list[int]) -> int | None:
    largest: int | None = None
    second: int | None = None
    for i in numbers:
        if largest is None or i > largest:
            second = largest
            largest = i
        elif i != largest and (second is None or i > second):
            second = i
    return second


def main() -> None:
    nums = [4, 2, 7, 4, 2, 9, 7]
    print("Original:", nums)
    print("Sin duplicados:", remove_duplicates(nums))
    print("Rotar izquierda k=2:", rotate_left(nums, 2))
    print("Rotar izquierda k=-2:", rotate_left(nums, -2))
    print("Rotar izquierda k=15:", rotate_left(nums, 15))
    print("Rotar izquierda k=0:", rotate_left(nums, 0))
    print("Rotar vacía:", rotate_left([], 3))

    evens, odds = split_even_odd(nums)
    print("Pares:", evens, "| Impares:", odds)

    a = [1, 3, 5, 8]
    b = [2, 3, 6, 7, 10]
    print("Mezcla ordenadas:", merge_sorted(a, b))

    print("Segundo mayor:", second_largest(nums))
    print("Todos iguales:", second_largest([5, 5, 5]))
    print("Lista vacía:", second_largest([]))


if __name__ == "__main__":
    main()