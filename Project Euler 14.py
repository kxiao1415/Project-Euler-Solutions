def collatzProblem(n):
    sequence = [n]
    while sequence[-1] !=1:
        if sequence[-1]%2==0:
            sequence.append(sequence[-1]/2)
        else:
            sequence.append(sequence[-1]*3+1)
    return sequence

maxLength = 1
maxNumber = 1
for  i in range(1,1000001):
    current = len(collatzProblem(i))
    if maxLength<current:
        maxLength=current
        maxNumber = i
        
print maxNumber, maxLength
