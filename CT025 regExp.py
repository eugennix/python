import sys
import re
# Выведите строки, содержащие слово,
# состоящее из двух одинаковых частей (тандемный повтор).
patt = r'\b(\w+)\1\b'
print(*[ln.strip() for ln in sys.stdin if re.search(patt, ln)], sep='\n')
