#mathmod lab2 var 8 Krazhevskiy
from puasson import puasson_gen, puasson_e, puasson_d
from binomial import bernoulli_gen, binomial_gen
from neg_binomial import neg_binomial_e, neg_binomial_gen, neg_binomial_d
from mcg import mcg
import matplotlib.pyplot as plt


if __name__ == '__main__':
    g = puasson_gen(3, mcg(2**31, 16807, 16807))
    seq = [n for n in g]
    #print(seq)
    plt.plot(seq)
    plt.show()

    Ep = puasson_e(3)
    Dp = puasson_d(3)
    print(Ep, Dp)

    '''
    g = binomial_gen(4, 0.25, mcg(2**31, 16807, 16807))
    seq = [n for n in g]
    plt.plot(seq)
    plt.show()
    #print(seq)
    '''

    g = neg_binomial_gen(6, bernoulli_gen(0.25, mcg(2**31, 16087, 16087, count=100000)))
    seq = [n for n in g]
    #print(seq)
    plt.plot(seq)
    plt.show()

    e = neg_binomial_e(6, 0.25)
    d = neg_binomial_d(6, 0.25)
