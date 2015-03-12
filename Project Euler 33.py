import fractions

result = [1,1]

for i in range(10,99):
    for j in range(i+1,100):
        if str(i)[1] != '0' and str(j)[1] !='0':
            for m in [0,1]:
                for n in [0,1]:
                    if str(i)[m] == str(j)[n] and float(i)/j == float(str(i)[(m+1)%2])/int(str(j)[(n+1)%2]):
                            result[0] *= i
                            result[1] *= j

print fractions.Fraction(result[0],result[1])
