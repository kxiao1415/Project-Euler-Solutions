def is_permutation(num1,num2):
    num1list = list(str(num1))
    num2list = list(str(num2))

    num1list.sort()
    num2list.sort()
    
    return num1list == num2list

stop = False
i = 100000

while not stop:
    if is_permutation(i, i*2) and is_permutation(i, i*3) and is_permutation(i, i*4) and is_permutation(i, i*5) and is_permutation(i, i*6):
        print i
        stop = True
    else:
        i += 1

    
