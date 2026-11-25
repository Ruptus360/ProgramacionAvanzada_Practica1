def format_monomial(coef, exp):
    if coef == 0:
        return ""

    sign = "+" if coef > 0 else "-"
    mag = abs(coef)

    if exp == 0:
        return f"{sign}{mag}"

    var_part = "x" if exp == 1 else f"x**{exp}"
    if mag == 1:
        return f"{sign}{var_part}"
    return f"{sign}{mag}{var_part}"


def format_polynomial(coefs):
    terms = []
    for i in range(len(coefs) - 1, -1, -1):
        monomial = format_monomial(coefs[i], i)
        if monomial:
            terms.append(monomial)

    if not terms:
        return "0"

    first = terms[0][1:] if terms[0].startswith("+") else terms[0]
    parts = [first]
    for i in terms[1:]:
        if i.startswith("+"):
            parts.append(f"+ {i[1:]}")
        else:
            parts.append(f"- {i[1:]}")

    return " ".join(parts)


def evaluate(coefs, x):
    if not coefs:
        return 0
    total = 0
    for i, c in enumerate(coefs):
        total += c * (x**i)
    return total


def derivative(coefs):
    if len(coefs) <= 1:
        return []
    return [i * coefs[i] for i in range(1, len(coefs))]


def main():
    coefs = [4.0, 1.0, 0.0, 2.0]
    poly_str = format_polynomial(coefs)
    print("Polinomio:", poly_str)
    print("Evaluado en x=2:", evaluate(coefs, 2))

    deriv = derivative(coefs)
    print("Derivada (coeficientes):", deriv)
    print("Derivada (formato):", format_polynomial(deriv))

    print("Polinomio nulo:", format_polynomial([0, 0.0, 0]))
    print("Constante [5] -> derivada:", derivative([5]))


if __name__ == "__main__":
    main()