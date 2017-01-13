old = 1
new = 1
sum = 0
while new < 4000000:
    next = new + old
#    print new
    if not (next & 1):
        print next
        sum += next
    old = new
    new = next
        
print sum
