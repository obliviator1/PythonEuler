def isprime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

l = []
x = 2
while len(l) < 10002:
    if isprime(x):
        l.append(x)
    x += 1

print l[10001]