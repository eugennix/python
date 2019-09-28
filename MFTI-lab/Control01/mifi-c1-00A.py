def check_limit(way1: list, way2: list, wm, hm) -> bool:
    # на дороге 1 ограничение веса, на д2 - высоты
    # вес складываем, высота - максимум
    w = sum([w for w, h in way1])
    h = max([h for w, h in way2])
    if w <= wm and h <= hm:
        return True

wt, ht, w1, h1, w2, h2, w_max, h_max = \
    list(int(input()) for n in range(8))

tr = (wt, ht)
g1 = (w1, h1 + ht)
g2 = (w2, h2 + ht)
# try variants
# везём сначала груз 1 - пианино
v1 = check_limit([tr, g1, g2], [tr, g2], w_max, h_max)

# везём сначала груз 2 - холодильник
v2 = check_limit([tr, g1], [tr, g1, g2], w_max, h_max)
print('YES' if v1 or v2 else 'NO')
