def is_anagram(word1: str, word2: str) -> bool:
    """Devuelve True si word1 y word2 son anagramas ignorando mayúsculas y espacios."""
    clean1 = "".join(sorted(word1.lower().replace(" ", "")))
    clean2 = "".join(sorted(word2.lower().replace(" ", "")))
    return clean1 == clean2


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Agrupa palabras que son anagramas manteniendo el orden de primera aparición."""
    groups: list[list[str]] = []
    for i in words:
        placed = False
        for j in groups:
            if is_anagram(i, j[0]):
                j.append(i)
                placed = True
                break
        if not placed:
            groups.append([i])
    return groups


def largest_group(groups: list[list[str]]) -> list[str]:
    """Devuelve el grupo más largo (el primero en caso de empate) o [] si está vacío."""
    if not groups:
        return []
    best = groups[0]
    for i in groups[1:]:
        if len(i) > len(best):
            best = i
    return best


def find_anagrams(word: str, words: list[str]) -> list[str]:
    """Devuelve los anagramas de word en words, excluyendo coincidencias exactas."""
    target = word.strip().lower()
    result: list[str] = []
    for i in words:
        if i.strip().lower() != target and is_anagram(word, i):
            result.append(i)
    return result


def main() -> None:
    words = ["roma", "amor", "ramo", "perro", "mora", "gato", "otro", "toga"]
    groups = group_anagrams(words)
    print("Grupos de anagramas:", groups)
    print("Grupo más grande:", largest_group(groups))
    print("Anagramas de 'roma' (excluyendo 'roma'):", find_anagrams("roma", words))

    extra_words = ["listen", "silent", "enlist", "Roma", "torta", "trato", "TORTA"]
    extra_groups = group_anagrams(extra_words)
    print("\nGrupos extra:", extra_groups)
    print("Grupo extra más grande:", largest_group(extra_groups))
    print("Anagramas de 'torta':", find_anagrams("torta", extra_words))
    print("Lista vacía -> largest_group:", largest_group([]))


if __name__ == "__main__":
    main()