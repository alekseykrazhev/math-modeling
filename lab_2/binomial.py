
def binomial_gen(n, p, random_generator):
    for r in random_generator:
        x = 0
        for _ in range(n):
            if r < p:
                x += 1
        yield x


def bernoulli_gen(p, random_generator):
    yield from binomial_gen(1, p, random_generator)
