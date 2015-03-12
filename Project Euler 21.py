#Project Euler 21
def properDivisorsSum(n):
    return sum([i for i in range(1,n/2+1) if n%i==0])
c=[]
for i in range(1,10000):
    if properDivisorsSum(i)!=i and properDivisorsSum(properDivisorsSum(i))==i:
        c+=[i]
print sum(c)
