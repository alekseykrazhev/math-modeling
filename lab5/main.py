# lab5 solving linear equations using Monte-Carlo method by Aleksey Krazhevskiy

import matplotlib.pyplot as plt
import numpy as np
from MonteCarlo import monte_carlo_solve, norm
import sympy as sp


if __name__ == '__main__':
    # data according to the task
    a = [[1.2, -0.3, 0.4],
         [0.4, 0.7, -0.2],
         [0.2, -0.3, 0.9]]

    f = [-4, 2, 0]

    # accurate solution = [-2.829, 5.143, 2.343]
    n = 3
    markov_len = 50
    markov_cnt = 1000

    # x = Bx + f
    b = [[-0.2, 0.3, -0.4],
         [-0.4, 0.3, 0.2],
         [-0.2, 0.3, 0.1]]
    # probability matrix
    p = [[1 / 3, 1 / 3, 1 / 3],
         [1 / 3, 1 / 3, 1 / 3],
         [1 / 3, 1 / 3, 1 / 3]]

    x = monte_carlo_solve(b, n, f, p, markov_len, markov_cnt)
    print(f"[1] Monte-Carlo method: x = {x}")

    # get an accurate solution using sumpy
    a1 = sp.Matrix(a)
    b1 = sp.Matrix(f)
    x1 = a1.inv() * b1
    print(f"[2] Accurate solution: x1 = {x1}")

    # difference between solutions
    print(f"[3] Norm of x-x1: {norm(x, x1, n)}")

    # task 3 - plot the solution
    X = np.loadtxt('Lab5Cnt.txt')
    Y = np.loadtxt('Lab5Len.txt')
    Z = np.loadtxt('Lab5Norms.txt')

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_trisurf(X, Y, Z, linewidth=0, antialiased=True)
    plt.show()
