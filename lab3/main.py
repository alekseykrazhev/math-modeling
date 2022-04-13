# mm lab3 var8 Krazhevskiy
import math
from normal import normal_generator
from mult_met import mcg
from laplace import laplace_generator
from exponential import exponential_generator
import matplotlib.pyplot as plt
from criteria import pearson_criterion, kolmogorov_criterion
from disp import expectation, dispersion


def test_criterion(criterion, params):
    try:
        return "PASS" if criterion(*params) else "FAIL"
    except (ArithmeticError, ValueError):
        return "NOT PASS"


def normal_distribution(x, mu, sigma2):
    sigma = math.sqrt(sigma2)
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))


def lognormal_distribution(x, mu, sigma2):
    return math.exp(normal_distribution(x, mu, sigma2))


def exponential_distribution(x, a):
    return a*math.exp(-a*x)


def laplace_distribution(x, a):
    return math.copysign(1, -x) * math.exp(-a * x) / 2


def weibull_distribution(x, a, b):
    return 1 - math.exp(-a * x ** b)



if __name__ == '__main__':

    #print('Normal distribution:')
    normally_distributed = normal_generator(mu=-5, sigma2=25,
                                            modulus=2 ** 31, a=16807, seed=16807,
                                            count=10000)
    #print(list(normally_distributed))
    seq = [g for g in normally_distributed]
    plt.plot(seq)
    plt.show()

    #print('Laplace distribution:')
    gen = mcg(modulus=2 ** 31, a=16807, seed=16807, count=1000)
    laplace_distributed = list(laplace_generator(1, gen))
    #print(laplace_distributed)
    seq = [g for g in laplace_distributed]
    plt.plot(seq)
    plt.show()

    #print('Exponential distribution:')
    gen = mcg(modulus=2 ** 31, a=16807, seed=16807, count=1000)
    exponentially_distributed = list(exponential_generator(4, gen))
    #print(exponentially_distributed)
    seq = [g for g in exponentially_distributed]
    plt.plot(seq)
    plt.show()

    mcg_params = dict(modulus=2 ** 31, a=16807, seed=16807, count=1000)
    distr = {"Normal distribution":
                 (normal_generator(mu=5, sigma2=25,
                                   **mcg_params), lambda x: normal_distribution(x, mu=5, sigma2=25)),
             "Exponential distribution":
                 (exponential_generator(4,
                                        mcg(**mcg_params)), lambda x: exponential_distribution(x, 4)),
             "Laplace distribution":
                 (laplace_generator(1,
                                    mcg(**mcg_params)), lambda x: laplace_distribution(x, 1)),}
    for name, (generator, func) in distr.items():
        print(name)
        seq = list(generator)
        if func:
            print("Pearson criterion:", test_criterion(pearson_criterion, (seq, 25, func)))
            print("Kolmogorov criterion:", test_criterion(kolmogorov_criterion, (seq, 25, func)))
        m = expectation(seq)
        print("Mean", m)
        print("Disp", dispersion(seq, m))
        print()
