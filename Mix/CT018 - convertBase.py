alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d_to10 = {sym: v for v, sym in enumerate(alpha)}
d_toAZ = {v: sym for sym, v in d_to10.items()}

'''
d_to10 = dict((chr(c), k) for k, c in enumerate(range(ord('0'), ord('9') + 1)))
d_to10.update((chr(c), k + 10) for k, c in enumerate(range(ord('A'), ord('Z') + 1)))
'''

def convertTo10(num, from_base=10):
    result = 0
    for s in (str(num)):
        result *= from_base
        result += d_to10[s]
    return int(result)


def convert(num, to_base=10, from_base=10):
    '''
    convert(num, to_base=10, from_base=10): возвращает строку.
    num (может быть int в десятичной системе счисления, либо строкой в произвольной)
    целочисленных 2 <= from_base, to_base <= 36
    основанием исходной и будущей систем отстчёта
    '''
    res = ''
    num = str(num).upper()
    # мой конвертор в 10
   # num10 = convertTo10(num, from_base)
    num10 = int(num, from_base)
    while num10:
        res = d_toAZ[num10 % to_base] + res
        num10 //= to_base
    return res

print(convert('34FD5', 18, 19))

