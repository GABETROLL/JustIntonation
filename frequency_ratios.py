def prime_factors(n: int, result: dict[int, int] = None) -> dict[int, int]:
    if not isinstance(n, int) or n < 2:
        raise ValueError(f"n must be an integer, and must be >= 2. Got: {n}")

    if result is None:
        result: dict[int, int] = {}

    for possible_factor in range(2, n):
        if n % possible_factor == 0:
            prime_factors(possible_factor, result)
            prime_factors(n // possible_factor, result)
            return result

    if n in result:
        result[n] += 1
    else:
        result[n] = 1

    return result


def simplify_fraction(integers: list[int]) -> list[int]:
    possible_factor: int = 2

    while True:
        for integer in integers:
            if possible_factor < integer:
                break
        else:
            break

        for integer in integers:
            if integer % possible_factor != 0:
                possible_factor += 1
                break
        else:
            for index in range(len(integers)):
                integers[index] //= possible_factor

    return integers


def make_co_prime(frequencies: list[int]) -> list[int]:
    return [simplify_fraction(beat_frequencies) for beat_frequencies in frequencies]


def convert_ratio_to_color(ratio: list[int]) -> int:
    product: int = 1

    for frequency in ratio:
        product *= frequency

    kelvin: int = (product - 1) * (12000 - 1000) / (1080 - 1) + 1000

    return kelvin
