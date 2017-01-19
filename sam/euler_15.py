mem = {}

def possible_paths(x_moves, y_moves):
    if x_moves == 0 or y_moves == 0:
        return 1
    try:
        return mem[(x_moves, y_moves)]
    except:
        r = possible_paths(x_moves - 1, y_moves) + possible_paths(x_moves, y_moves - 1)
        mem[(x_moves, y_moves)] = r
        return r

print possible_paths(20,20)
