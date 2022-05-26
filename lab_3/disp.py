def expectation(vec):
    res = 0
    for item in vec:
        res += item
    return res / len(vec)


def dispersion(vec, avg):
    res = 0
    for item in vec:
        res += pow(item - avg, 2)
    return res / (len(vec) - 1)
