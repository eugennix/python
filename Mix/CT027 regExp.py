import sys
import re
'''
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w
'''
txt = [ln.strip() for ln in sys.stdin]
print(*[re.sub(r'(\w)\1+', r'\1', ln) for ln in txt], sep='\n')


# :-)
#