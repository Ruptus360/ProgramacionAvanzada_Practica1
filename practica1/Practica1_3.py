def process_text(
    text: str = "This is a default text with Python and amazing words.",
    words_to_replace: list[str] = ["Python", "amazing"],
) -> tuple[str, int]:
    cleaned_text = text.strip().lower()
    target_words = {i.lower() for i in words_to_replace}

    words = cleaned_text.split()
    replaced_count = 0
    result_words: list[str] = []

    for i in words:
        if i in target_words:
            result_words.append("*" * len(i))
            replaced_count += 1
        else:
            result_words.append(i)

    processed_text = " ".join(result_words)
    return processed_text, replaced_count


def main() -> None:
    processed_text, count = process_text()
    print("Texto procesado:", processed_text)
    print("Palabras reemplazadas:", count)


if __name__ == "__main__":
    main()