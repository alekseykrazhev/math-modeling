
def lcg(modulus, a, c, seed, count=1000):
    for _ in range(count):
        seed = (a * seed + c) % modulus
        yield seed / modulus


def mcg(modulus, a, seed, count=1000):
    yield from lcg(modulus, a, 0, seed, count)
