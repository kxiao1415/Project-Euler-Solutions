#project euler 25

'''
compare to the second solution

a=1
c=1
b=0
n=1

while len(str(a))!=1000:
    a=a+b
    b=c
    c=a
    n+=1
'''

a=1
b=0
n=1

while len(str(a))!=1000:
    a, b=a+b,a
    n+=1
    
print n

'''
Pen and paper solution

F(n) = [Phi^(n)/sqrt(5)]

where the brackets means the closest integer.
Phi is defined as the golden ratio.

so, Phi^(n)/sqrt(5)>10^(999), solve for n.

'''
