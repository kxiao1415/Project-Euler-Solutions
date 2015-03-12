#project euler 37

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def isTruncatablePrime(n):
    n = str(n)
    for i in range(len(n)):
        if is_prime(int(n[i:])) == False or is_prime(int(n[:len(n)-i])) == False:
            return False
    return True

count = 0
n = 10
sum = 0

while count < 11:
    b = str(n)
    if b[0] in ['2','3','5','7'] and b[-1] in ['3','7','9']:
        if isTruncatablePrime(n):
            count += 1
            sum += n
    n +=1

print sum
    
    
