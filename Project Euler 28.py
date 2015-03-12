#Project Euler 28
 
def f(n):
    if n == 0:
        return 1
    else:
        return 4*((2*n+1)**2)-12*n
squareDiagonalSum = 0
for n in range(501):
    squareDiagonalSum+=f(n)
print squareDiagonalSum
'''
analytical solution:
f(n) = (16/3)*(n^3) + 10*n^2 + (26/3)*n + 1
squareDiagonalSum = f(500)
'''
