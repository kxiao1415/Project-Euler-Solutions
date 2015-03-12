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
print sum([i if len(primeFactorization(i))==1 else 0 for i in range(2000000)])
