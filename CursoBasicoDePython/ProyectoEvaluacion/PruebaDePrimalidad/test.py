def expand_x_1(n): 
# This version uses a generator and thus less computations
    c = 1
    for i in range(n//2+1):
        c = c*(n-i)//(i+1)
        print(c)
        yield c
 
def aks(p):
    if p==2:
        return True
 
    for i in expand_x_1(p):
        if i % p:
            print('Fail -> ',i)
    # we stop without computing all possible solutions

            return False
    return True
# https://rosettacode.org/wiki/AKS_test_for_primes#Python
