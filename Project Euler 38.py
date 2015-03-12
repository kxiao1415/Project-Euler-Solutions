#project euler 38

greatest = 0
result = []

#only need to check between 9234 and 10000
#we know the first digit is 9
#two digit number will not yield 9 digits
#same goes for 3 digit number
for i in range (9234,9387):
    n=1
    currentList = []
    while '0' not in currentList and len(set(currentList)) == len(currentList):
            currentList +=list(str(i*n))
            sortedCL = currentList[:]
            sortedCL.sort()
            if sortedCL == ['1','2','3','4','5','6','7','8','9']:
                currentValue = int(''.join(currentList))
                if  currentValue> greatest:
                    greatest = currentValue
                    result =[i,n]
                    break
            else:
                n +=1

print greatest, result
    
