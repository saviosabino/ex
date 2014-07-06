import sys
 
def prime(x):
    if x in [1,2,3]: return True 
    p = True 
    for i in range(1,x+1):
        if i != 1 and i != x:
            if x%i== 0: p = False 
    return p

def get_n_primes(n):
    primes = []
    c = 1
    while len(primes) < n:
        if prime(c): primes.append(c)
        c+=1
    return primes


#print prime(int(sys.argv[1]))
print get_n_primes(int(sys.argv[1]))


