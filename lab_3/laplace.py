from mult_met import mcg
import math


def laplace_generator(a, generator):
    for n in generator:
        if n < 0.5:
            yield math.log(2 * n) / a
        else:
            yield -math.log(2 * (1 - n)) / a
