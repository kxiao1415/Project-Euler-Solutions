#project euler 29

#Brute Force
result=[]
for i in range(2, 101):
    for j in range(2,101):
        term = i**j
        if term not in result:
            result += [term]
print len(result)
'''
Pen and Paper:
http://www.mathblog.dk/project-euler-29-distinct-terms-sequence-ab/
'''

