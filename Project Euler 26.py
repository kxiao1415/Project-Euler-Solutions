#project euler 26
def unitFraction(n):
    u=[]
    i=1
    while i%n not in u:
        u+=[i%n]
        i=(i*10)%n
    return len(u[u.index(i):])

max = 1
solution = 1
for i in range (1,1000):
    uf=unitFraction(i)
    if uf > max:
        max, solution = uf, i
print solution
