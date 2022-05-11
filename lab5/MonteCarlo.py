# Monte-Carlo method implementation for solving Ax = b

from numpy import random
from math import sqrt, pow


def norm(X, X1, n):
    return sqrt(sum([pow(X[i] - X1[i], 2) for i in range(n)]))


def markov_rand(P, state, size):
    rand = random.random()
    for i in range(size):
        rand -= P[state][i]
        if rand <= 0:
            return i
    return size - 1


def monte_carlo_solve(b, n, f, P, markov_len=50, markov_cnt=1000) -> list:
    """
    Solves the linear system x = Bx + f using the Monte-Carlo method
    :return list: x
    """
    solution = []
    for coordinate in range(n):
        x = 0
        for i in range(markov_cnt):
            prev_m = coordinate
            prev_q = 1
            for j in range(1, markov_len):
                next_m = markov_rand(P, prev_m, n)
                next_q = 0
                if P[prev_m][next_m] > 0:
                    next_q = prev_q * b[prev_m][next_m] / P[prev_m][next_m]
                x += next_q * f[next_m]
                prev_q = next_q
                prev_m = next_m
        solution.append(f[coordinate] + x / markov_cnt)
    return solution
