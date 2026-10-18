import re


def _only_digits(value: str) -> str:
    return re.sub(r"\D", "", value)


def is_valid_cpf(value: str) -> bool:
    """RN01: valida CPF pelos dígitos verificadores (módulo 11).

    Sequências com todos os dígitos iguais (ex: 111.111.111-11) são
    descartadas mesmo que matematicamente "fechem", pois são o falso
    positivo mais comum em textos de teste/exemplo.
    """
    digits = _only_digits(value)
    if len(digits) != 11:
        return False
    if digits == digits[0] * 11:
        return False

    def calc_digit(digs: str, weight_start: int) -> int:
        total = sum(int(d) * w for d, w in zip(digs, range(weight_start, 1, -1)))
        remainder = (total * 10) % 11
        return 0 if remainder == 10 else remainder

    d1 = calc_digit(digits[:9], 10)
    d2 = calc_digit(digits[:9] + str(d1), 11)
    return digits[-2:] == f"{d1}{d2}"


def is_valid_cnpj(value: str) -> bool:
    """RN02: valida CNPJ pelos dígitos verificadores (módulo 11, pesos específicos)."""
    digits = _only_digits(value)
    if len(digits) != 14:
        return False
    if digits == digits[0] * 14:
        return False

    def calc_digit(digs: str, weights: list) -> int:
        total = sum(int(d) * w for d, w in zip(digs, weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    d1 = calc_digit(digits[:12], weights1)
    d2 = calc_digit(digits[:12] + str(d1), weights2)
    return digits[-2:] == f"{d1}{d2}"
