import sys
import re

patt = r'\b(cat)\b'
print(*[ln.strip() for ln in sys.stdin if re.search(patt, ln)], sep='\n')


'''
[print(x.strip()) for x in __import__('sys').stdin if __import__('re').findall(r'\bcat\b', x)]
'''