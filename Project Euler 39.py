#project euler 39
#p has to be event
#let 'a' be the shortest side of the triagle, then a < p/3
#use (1)a**2 + b**2 = c**2 (2)a + b+ c = p to get b = (p**2-2*p*a)/(2*p-2*a)

count = 0
solution = 0

for p in range(2, 1001,2):
    currentCount = 0
    for a in range(1,p/3):
        if (p**2-2*p*a)%(2*p-2*a)==0:
            b = (p**2-2*p*a)/(2*p-2*a)
            c = p-a-b
            if a**2 + b**2 == c**2:
                currentCount +=1
    if count < currentCount:
        count = currentCount
        solution = p
        
print solution
