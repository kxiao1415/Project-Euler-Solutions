#solution to ponder this challenge June 2014
#http://domino.research.ibm.com/Comm/wwwr_ponder.nsf/Challenges/June2014.html
#uses numder 1,2,3,...,30

a=[[6,7,8,9,10],
   [11,12,13,14,15],
   [16,17,18,19,20],
   [21,22,23,24,25],
   [26,27,28,29,30]]


def offset(lis,offset):
    l=len(lis)
    b=[]
    for i in range(l):
        for j in range(l):
            b.append(lis[(j+i*offset)%l])
    return b

b=[]
for i in range(len(a)):
    b.append(offset(a[i],i))

for i in zip(*b):
    print i
