def isPalindromic(n):
    b=list(str(n))
    b.reverse()
    if list(str(n)) == b:
        return True
    else:
        return False

sum = 0
for i in range(1000001):
    if i%2 != 0 or i%10 != 0:
        if isPalindromic(i) and isPalindromic(bin(i)[2:]):
            sum += i

print sum
