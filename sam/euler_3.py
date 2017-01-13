
num = 600851475143

#primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

primes = [2, 3, 5, 7]

def is_prime(num, primes):
    for p in primes:
        if not (n % p):
            return False
    return True

for n in range(3,100000):
    if is_prime(n , primes):
        print "prime: {}".format(n)
        primes.append(n)


largest = 2
for p in primes:
    if not (num % p):
        print "remainder: {}, prime: {}, number: {}".format(num % p, p, num)
        num = num / p
