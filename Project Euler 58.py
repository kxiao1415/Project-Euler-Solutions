#Project Euler 58

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

ratio = 1
primeCount = 0
sideLength = 1

while ratio >= .1:
    sideLength += 2
    for i in range(sideLength**2, (sideLength**2)-3*(sideLength-1)-1, -sideLength+1):
        if is_prime(i):
            primeCount += 1

    ratio = float(primeCount) / (1+(sideLength-1)*2)

print sideLength
