#Project Euler 63
#10^(n-1) <= x^n < 10^n -->
#10^((n-1)/n) <= x < 10
#as n approaches infinity, 10^((n-1)/n) = 10

import math

n = 1
lower = 0
count = 0

while (lower < 10):
    lower = math.ceil(10 ** (float(n-1)/n))
    count += 10 - lower
    n += 1

print count
