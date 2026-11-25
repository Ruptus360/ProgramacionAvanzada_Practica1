def shift_char(char, shift):
    if len(char) != 1:
        return char

    if "a" <= char <= "z":
        base = ord("a")
        pos = (ord(char) - base + shift) % 26
        return chr(base + pos)

    if "A" <= char <= "Z":
        base = ord("A")
        pos = (ord(char) - base + shift) % 26
        return chr(base + pos)

    return char


def encrypt(text, shift):
    result = []
    for i in text:
        result.append(shift_char(i, shift))
    return "".join(result)


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(cipher_text):
    candidates = []
    for i in range(26):
        candidates.append(decrypt(cipher_text, i))
    return candidates


def main():
    plain_text = "Hola, Python! 123"
    shift = 29  # Equivale a 3 módulo 26

    encrypted = encrypt(plain_text, shift)
    decrypted = decrypt(encrypted, shift)

    print("Texto original:", plain_text)
    print(f"Cifrado (shift={shift}):", encrypted)
    print(f"Descifrado (shift={shift}):", decrypted)

    print("\nFuerza bruta sobre el texto cifrado:")
    for i, candidate in enumerate(brute_force(encrypted)):
        print(f"Clave {i:2d}: {candidate}")


if __name__ == "__main__":
    main()
