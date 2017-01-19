sum = 0
sum_square = 0
for x in range(1,101):
    sum += x
    sum_square += x*x

print sum*sum - sum_square
