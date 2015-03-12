def isPalindromic(a):
    c=[i for i in str(a)]
    b=c[:]
    c.reverse()
    if b==c:
        return True
    else:
        return False
   
LP=0

for i in range(100,1000):
    for j in range(100,1000):
        if i*j>LP and isPalindromic(i*j):
            LP = i*j

print LP
