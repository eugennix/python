# Найти 3 максимальных по произведению
# https://www.coursera.org/learn/python-osnovy-programmirovaniya/
# programming/HsPIC/naibol-shieie-proizviedieniie-triekh-chisiel

l = list(map(int, input().split()))

if len(l) > 2:
    great = 2**111
    mi1, mi2, ma1, ma2, ma3 = great, great, -great, -great, -great
    for x in l:
        if x > ma3:
            ma1, ma2, ma3 = ma2, ma3, x
        elif x > ma2:
            ma1, ma2 = ma2, x
        elif x > ma1:
            ma1 = x

        if x < mi2:
            mi1, mi2 = mi2, x
        elif x < mi1:
            mi1 = x

    if ma3*mi2*mi1 > ma3*ma2*ma1:
        print(mi2, mi1, ma3)
    else:
        print(ma1, ma2, ma3)
