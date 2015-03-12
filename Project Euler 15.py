#this is equivalent to permuation of 40 objects of 2 types, 20 from each type.
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result

print factorial(40)/(factorial(20)*factorial(20))
