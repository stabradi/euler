z = 0
for x in range(1000):
    if not ((x % 3) and (x % 5)):
        z += x

print z
