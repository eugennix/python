# Rome -> Arab
rome_arab = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
             'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
arab_rome = {v: k for k, v in rome_arab.items()}
ar_ro_sort = sorted(list(arab_rome.items()), reverse=True)

rom, decimal = input(), 0

while rom:
    if len(rom) > 1 and rom[:2] in rome_arab:
        decimal += rome_arab[rom[:2]]
        rom = rom[2:]
    elif rom[0] in rome_arab:
        decimal += rome_arab[rom[0]]
        rom = rom[1:]
    else:
        print('Bad sym', rom[0])
        rom = rom[1:]

print(decimal)


''' правильная версия

_rdecode = dict(zip('MDCLXVI', (1000, 500, 100, 50, 10, 5, 1)))
 
def decode( roman ):
    result = 0
    for r, r1 in zip(roman, roman[1:]):
        rd, rd1 = _rdecode[r], _rdecode[r1]
        result += -rd if rd < rd1 else rd
    return result + _rdecode[roman[-1]]
 
if __name__ == '__main__':
    for r in 'MCMXC MMVIII MDCLXVI'.split():
        print( r, decode(r) )
        
        
        '''

'''
Римские цифры читаются слева направо, когда вы добавляете или вычитаете значение каждого символа.

Если значение ниже, чем следующее значение, оно будет вычтено. В противном случае это будет добавлено.

Например, мы хотим преобразовать римскую цифру MCMLIV в арабское число:

M = 1000 must be added, because the following letter C =100 is lower.
C = 100 must be subtracted because the following letter M =1000 is greater.
M = 1000 must be added, because the following letter L = 50 is lower.
L = 50 must be added, because the following letter I =1 is lower.
I = 1 must be subtracted, because the following letter V = 5 is greater.
V = 5 must be added, because there are no more symbols left.
Теперь мы можем рассчитать число:

1000 - 100 + 1000 + 50 - 1 + 5 = 1954 
ссылка: http://www.mathinary.com/roman_numerals_from_roman_numerals_to_arabic_numbers.jsp

def from_roman(num):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i,c in enumerate(num):
        if (i+1) == len(num) or roman_numerals[c] >= roman_numerals[num[i+1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result'''