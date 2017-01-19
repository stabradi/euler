memoization = {}
def collatz(n):
    try:
        return memoization[n]
    except:
        if n == 1:
            return 1
        if n & 1:
            x = 1 + collatz(3 * n + 1)
        else:
            x = 1 + collatz(n/2)
        memoization[n] = x
        return x

biggest = 0
for n in range(1,999999):
    current = collatz(n)
    if current > biggest:
        biggest = current
        print "n({}) is {}".format(n, biggest)


