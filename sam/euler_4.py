def is_palendrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

result = ""
largest_product = 0

for x in range(999,99, -1):
    for y in range(x, 99, -1):
        if is_palendrome(x*y):
            if largest_product < x*y:
                largest_product = x*y
                result = "{}, {}".format(x, y)

print result
