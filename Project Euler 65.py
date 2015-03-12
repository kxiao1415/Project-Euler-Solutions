#project euler 65

e = [2]
for i in range(1, 34):
    e += [1,2*i,1]

def fractionExpand(fr):
    if len(fr) == 1:
        return fr[0]
    else:
        return fr[0]+1/(float(fractionExpand(fr[1:])))
    
print fractionExpand(e)

'''
Solution # 1:
n0, n1, L = 1, 2, 100

for i in range(2, L):
    n1, n0 = n0, n1 + n0 * (1 if i % 3 else 2 * i//3)

print L,"convergent for e =", sum(map(int, str(n0)))
'''
