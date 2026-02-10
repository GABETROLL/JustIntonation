from math import log2, log


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


def graph(a: int, b: int) -> tuple[float, float]:
    """
    For any frequency F as a point in the 2D cartesian plane,
    another frequency G can be made such that G = rF, and
    the point in the cartesian plane corresponding to G
    is derived from the ratio r and F's position.
    G / F = r.

    Then, both F and G can be multiplied by another ratio
    s to create H and I, where Fs = H and Gs = I,
    and the distance between F and H, and G and I should be the same,
    and the angle of the line from H to H and G to I should be the same,
    and the angle of said lines against the line from F to G must be the same.

    Then, the ratio from H to I IS the ratio from F to G,
    since G / F = r, H = Fs, I = Gs, which means I / H = (Gs) / (Fs) = G / F = r.

    Therefore, if this graph is built correctly, by multiplying H
    by r to equal I, the corresponding distance between points H and I
    in the cartesian plane must be the same as the distance from F to G,
    as well as the angle of the lines F-to-G and H-to-I.

    This `graph` function uses `a` and `b` as the ratio r multiplied
    by some point F in the cartesian plane representing a frequency,
    such that graph(a, b) = (x, y), where F + (x, y) = (the point in the cartesian plane
    representing frequency G).
    """

    """
    Interpreting r and s as 2D vectors in the cartesian plane, R + S = S + R,
    because F * r * s = F * s * r. (I = F * r * s, H = F * s, and H * r = I,
    therefore F * s * r = I, and therefore, F * r * s = F * s * r)

    Therefore, there is some mapping r => R and s => S, such that
    (ar / br) => (xr, yr), (as / bs) => (xs, ys), and (xr, yr) + (xs, ys) = (xs, ys) + (xr, yr)
    = (xr + xs, yr + ys) <= (ar * as) / (br * bs).

    These points and vectors form a closed set under addition!
    As well as the frequencies and ratios, which also form a closed set, under multiplication!

    Let's try this approach:

    The frequency ratio a / b can be represented in the cartesian plane as (log2(a / b), log3(a / b)).

    I suspect loga(r) / logb(r) is always equal to some fixed real number, when r is real:

    loga(a ** x) / logb(a ** x) = x / logb((b ** y) ** x) = x / logb(b ** (y * x))
    = x / (y * x) = 1 / y = 1 / logb(a) <-- CONSTANT!!!

    This makes it difficult to use to graph notes, because they all end up on a single line.

    Approach 2:
    Make the x and y axii correspond to two different logarithmic scales,
    where a note multiplied by a is moved ONLY in one axis, and multiplied by
    b, moves ONLY in the other axis, by the distance of loga(r) or logb(r)
    respectively. Then, for every other ratio of frequencies r,
    make the line move in each corresponding axis the amount needed
    so that the coordinates match loga(F * r) and logb(F * r), where
    F is the frequency (Hz).

    I choose y axis to be 2, and x axis to be 3 / 2.
    """
    ratio: float = a / b
    x_log: float = log(ratio, 3 / 2)
    y_log: float = log2(ratio)

    return (
        0 if y_log % 1 == 0 else x_log,
        0 if x_log % 1 == 0 else y_log,
    )
