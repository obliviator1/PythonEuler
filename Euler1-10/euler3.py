from math import sqrt
# def factor2(x):
#     faclist=[]
#     num = int(x**0.5)
#     for i in range(num,2,-1):
#         if x % i == 0:
#             faclist.append(i)
#     for c in faclist:
#             sorted(faclist)
#             print faclist

primes = [2]
value = 3
number = 600851475143
while value < sqrt(number):
    isPrime = True
    for i in primes:
        if  not value % i:
            isPrime = False
            value += 2
    if isPrime:
        primes.append(value)
        if number % value == 0:
            print value
            number /= value
print number
print sorted(primes)