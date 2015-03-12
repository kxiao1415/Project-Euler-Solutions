#project euler 56

def digitalSum(num):
    return sum([int(i) for i in str(num)])

maximum = 0
for i in range (1, 100):
    for j in range (1, 100):
        ds = digitalSum(i**j)
        if ds > maximum:
            maximum = ds

print maximum
    
