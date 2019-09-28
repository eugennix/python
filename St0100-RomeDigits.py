"""
Будем использовать вариант, в котором числа
4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего:
IV, IX, XL, XC, CD и CM, соответственно.

Строка, содержащая натуральное число n, 0<n<4000.
Строка, содержащая число, закодированное в римской системе счисления.
"""
rome_arab = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
             'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
             'D': 500, 'CM': 900, 'M': 1000}
arab_rome = {v: k for k, v in rome_arab.items()}
ar_ro_sort = sorted(list(arab_rome.items()), reverse=True)

def get_max_rome(num):
    for ar, ro in ar_ro_sort:
        if num >= ar:
            return ar, ro

test = 3212
result = []
while test:
    arab, rome = get_max_rome(test)
    test -= arab
    result.append(rome)
print(''.join(result))


'''
d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
n = int(input())
for i in d:
    if n // i != 0:
        print(d[i]*(n // i), end='')
        n %= i


def checkio(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
        # print('({}) {} => {}'.format(roman, n, result))
    return result


def checkio(data):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]
    
    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o =  ones[data % 10]
    
    return t+h+te+o
    
https://habr.com/ru/post/311678/
    
def checkio(data):
    base = "I"*data
    
    base = base.replace("I"*5, "V")
    base = base.replace("V"*2, "X")
    base = base.replace("X"*5, "L")
    base = base.replace("L"*2, "C")
    base = base.replace("C"*5, "D")
    base = base.replace("D"*2, "M")
    
    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")
    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")
    
    return base
'''