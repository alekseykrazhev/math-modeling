# lab4 Monte-Carlo method implementation by Aleksey Krazhevkiy

from MonteCarlo import monte_carlo, monte_carlo_double, compare_to_solution
from math import e, tan
import matplotlib.pyplot as plt


if __name__ == '__main__':
    integral1 = monte_carlo(0, 2, lambda x: ((e ** (-x)) * (1 + x) ** 0.5), 1000)
    print(f"1. {integral1}")

    integral2 = monte_carlo_double(0, 1, 0, 2, lambda x, y: x ** 2 + y ** 2, 1000)
    print(f"2. {integral2}")

    # compare monte-carlo1 result to solution = 1.11007
    seq1 = []
    for i in range(1000, 10000, 50):
        seq1.append(compare_to_solution(monte_carlo(0, 2, lambda x: ((e ** (-x)) * (1 + x) ** 0.5), i), 1.11007))

    plt.plot(seq1)
    plt.title("Monte-Carlo method 1")
    plt.xlabel("Iterations (1000 + x*50)")
    plt.ylabel("Precision")
    plt.show()

    # compare monte-carlo2 result to solution = 3.3333333333
    seq2 = []
    for i in range(1000, 10000, 50):
        seq2.append(compare_to_solution(monte_carlo_double(0, 1, 0, 2, lambda x, y: x ** 2 + y ** 2, i), 3.3333333333))

    plt.plot(seq2)
    plt.title("Monte-Carlo method 2")
    plt.xlabel("Iterations (1000 + x*50)")
    plt.ylabel("Precision")
    plt.show()
