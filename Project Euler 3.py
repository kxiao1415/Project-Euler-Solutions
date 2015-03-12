def primeFactorization(n):
    i = 2
    primeFactor = []

    while i*i <= n:
        while n%i==0:
            n=n/i
            primeFactor += [i]
        i +=1

    if n > 1:
        primeFactor +=[n]

    return primeFactor

print primeFactorization(600851475143)[-1]
