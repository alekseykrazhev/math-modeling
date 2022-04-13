#lab 1 var 8 Krazhevskiy
import math
from random import random
import numpy as np


#константы
k = 256
a0 = 262147
b = a0
M = math.pow(2, 31)


now = a0
def mult_cong_met():
    global now
    now = (now * b) % M
    return now / M


v = []
def first():
    for _ in range(k):
        v.append(mult_cong_met())


def maclaren():
    indx = int(random() % k)
    num = v[indx]
    v[indx] = mult_cong_met()
    return num


'''
v - объем выборки
n - количество разбиений (0,1)
c - критическое значение лямбда = 1.36 для 0,05 
func - закон распределения СВ

sqrt(v) * Dn <= LAMBDAa, где
Dn = max|Fn(x) - F(x)|
'''
def kolmogorov(v, n, c, func):
    print ('Working', end = '')
    cof = 0
    for i in range (n):
        count = 0
        for _ in range (v):
            if func() < float(i / n):
                count += 1
        #print (i, ': ', count)
        print('.', end = '')

        f = float(count / v)
        if cof < abs(f - i / n):
            cof = abs(f - i / n)
        '''
        if cof < max(i / n - f, f - (i - 1) / n):
            cof = max(i / n - f, f - (i - 1) / n)
        '''
    #print (math.sqrt(v) * cof)
    if math.sqrt(v) * cof < c:
        return 'pass'
    else:
        return 'not pass'


'''
ans = (Oi - Ei)^2 / Ei
'''
def pirson(v, n, c, func):
    arr = np.zeros(n+1, dtype = int)

    #подсчет числа степеней свободы
    for _ in range (v):
        a = round(func() * n)
        arr[a] += 1

    #подсчет ответа по формуле
    ans = 0
    for i in range(n):
        ans += math.pow(arr[i] - v/n, 2) / (v/n)
    #print (ans)
    if ans < c:
        return 'pass'
    else:
        return 'not pass'


if __name__ == '__main__':
    fout1 = open ('out1.txt', 'w')
    fout2 = open ('out2.txt', 'w')
    fout3 = open ('test_res.txt', 'w')
    first()

    for _ in range (1000):
        fout1.write(str(mult_cong_met()))
        fout1.write('\n')

    for _ in range (1000):
        fout2.write(str(maclaren()))
        fout2.write('\n')

    fout1.close()
    fout2.close()

    fout3.write('Test Results:\n')
    fout3.write('\tKolmogorov for maclaren:\n')
    fout3.write(kolmogorov (20000, 250, 1.36, maclaren))
    fout3.write('\n\tPirson for maclaren:\n')
    fout3.write(pirson (1000, 25, 37.6525, maclaren))

    fout3.close()