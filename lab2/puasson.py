import math


def puasson_gen(lambd, random_generator):
    for r in random_generator:
        p = math.exp(-lambd)
        a = 1.0
        x = 0

        while True:
            x += 1
            a *= r
            if a <= p:
                break

        yield x - 1

def puasson_e(lam):
    return lam
  

def puasson_d(lam):
    return lam