#project euler 20
 
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return str(result)
solution = 0

for i in factorial(100):
    solution +=int(i)

print solution
