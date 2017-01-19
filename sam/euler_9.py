for c in range(1000, 2, -1):
    c2 = c*c
    for b in range(c - 1, 1, -1):
        b2 = b*b
        for a in range(b - 1, 0, -1):
            if a*a + b2 == c2:
                if a + b + c == 1000:
                    print "a: {}, b: {}, c: {}".format(a,b,c)
                    print a*b*c
                    break

