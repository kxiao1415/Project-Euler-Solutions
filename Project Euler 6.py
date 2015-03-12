#Brute Force way
'''
sumSquare = 0
listSum = 0
for i in range(1, 101):
    sumSquare +=i**2
    listSum +=i
print listSum**2-sumSquare
'''
#More elegant: squareSum = (n*(n+1)/2)**2, sumSquare = n*(n+1)*(2n+1)/6
print(((100*(100+1))/2)**2 - (100*(100+1)*(2*100+1))/6)
