def projectEuler1 (n):
    totalsum = 0
    for i in range (1,n):
        if i%3 == 0 or i%5 == 0:
            totalsum +=i
    return totalsum

print projectEuler1(1000)
        
