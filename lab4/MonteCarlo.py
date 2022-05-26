# file for Monte Carlo implementation
import numpy as np


def monte_carlo(left_bound, right_bound, function, n) -> float:
    """
    Monte-Carlo method implementation
    returns the value of the integral
    """
    sum_ = 0
    for i in range(n):
        sum_ += function(np.random.uniform(left_bound, right_bound)) * (right_bound - left_bound)

    return sum_ / n


def monte_carlo_double(left_bound1, right_bound1, left_bound2, right_bound2, function, n) -> float:
    """
    Monte-Carlo method implementation for double integration
    returns the value of the integral
    """
    sum_ = 0

    for i in range(n):
        u1 = np.random.uniform(left_bound1, right_bound1)
        u2 = np.random.uniform(left_bound2, right_bound2)

        sum_ += function(u1, u2) * (right_bound1 - left_bound1) * (right_bound2 - left_bound2)

    return sum_ / n


def compare_to_solution(generated_value, solution_value) -> float:
    """
    Compare generated value with solution value
    returns precision
    """
    return abs(generated_value - solution_value)
