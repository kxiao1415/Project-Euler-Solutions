def solution9():
    for i in range(1000):
        for j in range(i):
            for k in range(i):
                if j**2 + k**2 == i**2 and i + j + k == 1000:
                    return [i,j,k]
print solution9()
