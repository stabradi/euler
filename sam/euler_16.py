import math

n = int(math.pow(2,1000))
s = 0
while n > 9:
    s += n % 10
    n = n/10
    print n
    
print s+n
