def lcg(modulus, a, c, seed, count=100):
    """Linear congruential generator."""
    for i in range(count):
        seed = (a * seed + c) % modulus
        yield seed / modulus


def mcg(modulus, a, seed, count=100):
    """Multiplicative congruential generator."""
    yield from lcg(modulus, a, 0, seed, count)
