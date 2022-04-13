from mult_met import mcg
import math


def laplace_generator(a, generator):
    for n in generator:
        if n < 0.5:
            yield math.log(2 * n) / a
        else:
            yield -math.log(2 * (1 - n)) / a


if __name__ == "__main__":
    gen = mcg(modulus=2 ** 31, a=16807, seed=16807, count=1000)
    laplace_distributed = list(laplace_generator(0.5, gen))
    print(laplace_distributed)
