#Project Euler 35
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def circularPrime(n):
    b = str(n)
    for i in range(len(b)):
        if is_prime(int(b))==False:
            return False
        b = b[-1] + b[:-1]
    return True

solution = 0
for i in range (1000001):
    if circularPrime(i):
        solution +=1

print solution
