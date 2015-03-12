#Project Euler 24

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                
a=list(all_perms([0,1,2,3,4,5,6,7,8,9]))
a.sort()
print a[999999]
