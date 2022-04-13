from mult_met import mcg
import math


def normal_generator(mu, sigma2, modulus, a, seed, count):
    sequence = list(mcg(modulus, a, seed, count * 12))
    for i in range(count):
        yield mu + math.sqrt(sigma2) * sum(sequence[12 * i + j] for j in range(12)) - 6

