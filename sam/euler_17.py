# one   3
# two   3
# three 5
# four  4
# five  4
# six   3
# seven 5
# eight 5
# nine  4

# ten       3
# eleven    6
# twelve    6
# thirteen  8
# fourteen  8
# fifteen   7
# sixteen   7
# seventeen 9
# eighteen  8
# nineteen  8

# twenty  6
# thirty  6
# forty   5
# fifty   5
# sixty   5
# seventy 7
# eighty  6
# ninety  6

# hundred 7

# onethousand

number_map = [0,3,3,5,4,4,3,5,5,4 ,3,6,6,8,8,7,7,9,8,8]
tens_map = [0,0,6,6,5,5,5,7,6,6]

def below_100(n):
    print "below 100 {}".format(n)
    if n < 20:
        return number_map[n]
    return number_map[n%10] + tens_map[n/10]

def letter_count(n):
    if n > 999:
        return 11
    if n % 100 == 0:
        return number_map[n/100] + 7
    if n < 100:
        return below_100(n%100)
    return number_map[n/100] + 10 + below_100(n%100)

sum = 0
for i in range(1,1001):
#    print("{}: {}".format(i, letter_count(i)))
    sum += letter_count(i)
print sum
