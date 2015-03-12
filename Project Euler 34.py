def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result

solution = 0

# 2540161 = 9!*7+1
for i in range (10,2540161):
    factorialSum = 0
    for j in str(i):
        factorialSum += factorial(int(j))
    if i == factorialSum:
        solution += i

print solution
        
