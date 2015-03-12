#Solution 1. slow
'''
def fibonacci(n):
    assert n >-1
    if n ==1 or n == 0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibonacciList=[]
terms = 1
a = fibonacci(terms)

while a<4000001:
    if a%2==0:
        fibonacciList+=[a]
    terms +=1
    a = fibonacci(terms)

print sum(fibonacciList)
'''

#Solution 2: a much faster solution

fib1 = 1
fib2 = 2
total = 0

while fib2 <= 4*10**6:
    if fib2 % 2 == 0:
        total += fib2
    fib1, fib2 = fib2, fib1 + fib2

print total
