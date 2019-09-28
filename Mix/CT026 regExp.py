import sys
import re
txt = [ln.strip() for ln in sys.stdin]
print(*[re.sub(r'human', r'computer', ln) for ln in txt], sep='\n')


# :-)
# print(re.sub(r'human', 'computer', sys.stdin.read()), end='')
