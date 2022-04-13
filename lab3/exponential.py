import math


def exponential_generator(a, generator):
    for n in generator:
        yield -math.log(n) / a
