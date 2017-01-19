primes = [2, 3, 5, 7]

def is_prime(num, primes):
    for p in primes:
        if not (n % p):
            return False
    return True

for n in range(3,2000001):
    if is_prime(n , primes):
        print "prime: {}".format(n)
        primes.append(n)

print reduce(lambda x, y: x+y, primes)
