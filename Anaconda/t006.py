k, up, dn, monoM, isFirst = 0, 0, 0, 0, 1
while True:
    k1 = int(input())
    if k1 == 0:
        break
    if k1 == k:
        if max(up, dn) > monoM:
            monoM = max(up, dn)
        up, dn = 0, 0
        # print('=', up, dn)
    elif k1 > k:
        up += 1
        if dn > monoM:
            monoM = dn
        dn = 1
        # print('>', up, dn)
    else:
        dn += 1
        if up > monoM:
            monoM = up
        up = 1
        # print('<', up, dn)
    k = k1
    if isFirst:
        up, dn, monoM, isFirst = 1, 1, 1, 0

print(max(monoM, up, dn))
