import math


def empirical(x, seq):
    res = 0
    for item in seq:
        if item < x:
            res += 1
    return res / len(seq)


def kolmogorov_criterion(seq, parts, distr_func):
    lo = min(seq)
    step = (max(seq) - min(seq)) / parts
    dn = 0
    for i in range(1, parts + 1):
        point = lo + i * step
        temp = math.fabs(empirical(point, seq) - distr_func(point))
        if dn < temp:
            dn = temp
    return math.sqrt(len(seq)) * dn < 1.36


def pearson_criterion(seq, parts, distr_func):
    lo = min(seq)
    if lo >= 0:
        lo = 0
    step = (max(seq) - lo) / parts
    frequency = [0] * parts
    for item in seq:
        index = int((item - lo) / step)
        if index == parts:
            index -= 1
        frequency[index] += 1
    res = 0
    for i in range(1, parts + 1):
        delta = len(seq) * (distr_func(lo + i * step) - distr_func(lo + (i - 1) * step))
        res += pow((frequency[i - 1] - delta), 2) / delta
    return res < 37.7
