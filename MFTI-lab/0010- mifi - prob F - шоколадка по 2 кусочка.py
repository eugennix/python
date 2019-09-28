#n1 2 3 4
# 0 3 6 9
# 1 4 7 10
# 2 5 8 11 ...

# 2 -> 3
# 4 -> 11
# 10 -> 571
# 1 -> 0
# 117 -> 0
# 10000 -> .....


place_count = 0
def get_free_near_pos(from_pos):
    x = from_pos // 3
    y = from_pos % 3
    if y and not from_pos - 1 in used:
        yield (from_pos - 1)
    if x < n -1 and not from_pos + 3 in used:
        yield (from_pos + 3)
    if y < 2 and not from_pos + 1 in used:
        yield (from_pos + 1)
    if x and not from_pos - 3 in used:
        yield (from_pos - 3)

def is_posible_place():
    for x in not_used:
        if list(get_free_near_pos(x)):
            return True
    return False

def place_domino(pos):
    # print('in', pos)
    global place_count
    free_near = list(get_free_near_pos(pos))
    for other_pos in free_near:
        used.add(pos)
        used.add(other_pos)
        not_used.remove(pos)
        not_used.remove(other_pos)
        print('place >', pos, other_pos)
        next_moves = list(get_free_near_pos(other_pos))
        for next_place in next_moves:
            # print('try > ', next_place)
            place_domino(next_place)
        if not is_posible_place():
            place_count += 1
            print(' found ', place_count)
        print('remove >', pos, other_pos)
        used.remove(other_pos)
        used.remove(pos)
        not_used.add(pos)
        not_used.add(other_pos)

def chocko_3xN_permutation(n):
    if n % 2 or n < 1:
    # для нечётного n плитка не делится по 2 кусочка
    if n == 2:
        return 3
    if n == 4:
        return 11:

n = int(input())
i
    print(0)
else:
    permutation_of_2x3 = 3
    total = 3
    # прибавляем по 2 ряда
    for i in range(n//2 - 1):
        # 3 варианта без вмешательство в ранние ряды +
        #
        total = total * (permutation_of_2x3) + 2)

'''    
    not_used = set([x for x in range(n * 3)])
    used = set()
    place_domino(0)
    print('result = ', place_count)
'''