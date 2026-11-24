def normalize(text: str) -> str:
    clean = text.lower()
    replacements = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ü": "u",
    }
    for src, dst in replacements.items():
        clean = clean.replace(src, dst)
    return "".join(i for i in clean if i.isalnum())


def is_palindrome(text: str) -> bool:
    normalized = normalize(text)
    return normalized == normalized[::-1]


def find_palindromes(sentences: list[str]) -> list[str]:
    return [i for i in sentences if is_palindrome(i)]


def palindrome_words(text: str) -> list[str]:
    result: list[str] = []
    for i in text.split():
        word_norm = normalize(i)
        if len(word_norm) >= 3 and word_norm == word_norm[::-1]:
            result.append(i)
    return result


def main() -> None:
    sentences = [
        "Anita lava la tina",
        "Dábale arroz a la zorra el abad",
        "Reconocer",
        "Hola mundo",
        "La ruta nos aporto otro paso natural",
    ]

    print("Palíndromos encontrados:")
    for i in find_palindromes(sentences):
        print(" -", i)

    sample_phrase = "Ana y radar salieron con oso y civic a pasear"
    print("\nPalabras palíndromas (3+ letras):", palindrome_words(sample_phrase))


if __name__ == "__main__":
    main()