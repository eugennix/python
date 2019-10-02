'''
 Найти 2 максимальных по произведению
'''

l = list(map(int, input().split()))

if len(l) > 1:
    great = 2**111
    mi1, mi2, ma1, ma2 = great, great, -great, -great
    for x in l:
        if x > ma2:
            ma1, ma2 = ma2, x
        elif x > ma1:
            ma1 = x
        if x < mi2:
            mi1, mi2 = mi2, x
        elif x < mi1:
            mi1 = x
    if mi1*mi2 > ma1*ma2:
        print(mi2, mi1)
    else:
        print(ma1, ma2)
