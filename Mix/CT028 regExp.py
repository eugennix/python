import sys
import re
'''
Выведите строки, содержащие двоичную запись числа, кратного 3.
Двоичной записью числа называется его запись в двоичной системе счисления.
не используя int()
'''
#txt = [x.strip() for x in sys.stdin]
#tx2 = [x for x in txt if re.fullmatch(r'[01]+', x)]
#print(tx2)
# print(*[x for x in txt if re.match(r'^[01]+$', x) and \
#        not int(x, base=2) % 3], sep='\n')

'''
txt = [x.strip() for x in sys.stdin]
tx2 = [x.lstrip('0') for x in txt if re.fullmatch(r'[01]+', x)]
p = r'^0*((1(01*0)*1)*0*)*$'
p = r'^(0|1(01*0)*1)*$'
'''

# print(*[x for x in tx2 if re.match(p, x)], sep='\n')
# шаблон делимости на 3
# patt = r'^((0*)((11)*)((1((00)*)1)*)(101*(0|((00)*1*)*0)1)*(1(000)+1*01)*)*$'

# p = r'0*((1(01*0)*1)*0*)*'
p = r'^(0|1(01*0)*1)$*'
for i in range(1, 100000):
    x = str(bin(i))[2:]
    x = x.replace()
    test = re.fullmatch(p, x)
    if (i % 3 == 0) ^ (test is not None):
        print(i, '  ',i%3,'   ', x, '  ', test)



# print(*[x for x in tx2 if re.fullmatch(p, x)], sep='\n')

#      0*((1(01*0)*1)*0*)*
#
# Using some basic regex rules, this simplifies to
#
# (1(01*0)*1|0)*
#
# Have a nice day.