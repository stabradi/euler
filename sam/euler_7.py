primes = [2, 3, 5, 7]

def is_prime(num, primes):
    for p in primes:
        if not (n % p):
            return False
    return True

prime_count = 4
n = 7
while True:
    n += 1
    if is_prime(n , primes):
        #print "prime: {}".format(n)
        primes.append(n)
        prime_count += 1
        if prime_count > 10000:
            print primes[-1]
            break
