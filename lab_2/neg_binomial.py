
def neg_binomial_gen(r, random_generator, count=1000):
    ''' Y = inf{n | Sn = r} - r '''
    for _ in range(count):
        sn = 0
        indx = 0
        n = -1

        for rand in random_generator:
            #print (rand)
            sn += rand
            if sn == r:
                n = indx
                break
            indx += 1

        yield n - r


def neg_binomial_d(r, p):
    return r * (1-p) / (p ** 2)


def neg_binomial_e(r, p):
    return r * (1-p) / p
