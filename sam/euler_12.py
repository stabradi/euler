import math

def count_divisors(x):
    count = 0
    for n in range(1, int(math.sqrt(x)) + 1):
        if x % n == 0:
            if x/n == n:
                count += 1
            else:
                count += 2
    return count

n = 1
tri = 1
while True:
    n += 1
    tri += n
    d = count_divisors(tri)
    if d > 250:
        print "{} {}".format(tri, count_divisors(tri))
    if d > 500: 
        print tri
        break
