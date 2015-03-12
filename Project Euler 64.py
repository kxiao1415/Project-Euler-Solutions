#Project Euler 64
'''
continued fraction expansion section of this wiki page provides the algorithm for finding a's:
http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
corollary 3.3 from this paper provides the periodicity:
http://web.math.princeton.edu/mathlab/jr02fall/Periodicity/alexajp.pdf
'''
import math

def fractionExpansion(num):
    a0 = int(math.sqrt(num))
    a = a0
    m = 0
    d = 1
    cfr = [a0]
    while (a != 2*a0):
        m = d*a - m
        d = (num - m**2)/d
        a = int((a0 + m)/d)
        cfr.append(a)
    return cfr

count = 0
for i in range(2, 10000):
    if int(math.sqrt(i)) ** 2 != i:
           if (len(fractionExpansion(i))-1) % 2 == 1:
               count += 1

print count
