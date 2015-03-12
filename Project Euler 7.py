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

#A number is prime if the length of its primeFactorization returns 1

count = 0
n=2
while count <10001:
    pf = primeFactorization(n)
    if len(pf) == 1:
        count +=1
    n+=1

print n-1
