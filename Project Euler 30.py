#Project Euler 30
upperBound = 6*(9**5)
result = []
for i in range(10,upperBound+1):
    digitSum = 0
    for j in str(i):
        digitSum += int(j)**5
    if digitSum == i:
        result +=[i]
print sum(result)
